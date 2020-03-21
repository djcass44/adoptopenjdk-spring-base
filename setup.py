import subprocess
import os


def dir_and_write(filename: str, data: str):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(data)


jdks = [11, '11-openj9', 12, '12-openj9', 13, '13-openj9', 14, '14-openj9']
distros = ['alpine', 'debian']

versions = {
    'alpine': ['slim', 'jre'],
    'debian': ['slim', 'jre'],
    # 'ubi-minimal': ['-jre', '']
}

dockerfiles = {
    'alpine': """FROM ${version}
LABEL maintainer='Django Cass <django@dcas.dev>'

# update packages and install tomcat-native
RUN apk upgrade --no-cache -q && \\
    apk add --no-cache tomcat-native
    """,
    'debian': """FROM ${version}
LABEL maintainer='Django Cass <django@dcas.dev'

# update packages and install tomcat-native
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq libtcnative-1 && \
    apt-get clean -y && \
    apt-get autoclean -y && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*
    """
}

build = """---
kind: pipeline
name: ${version}

steps:
  - name: slim
    image: plugins/docker
    settings:
      repo: djcass44/adoptopenjdk-spring-base
      dockerfile: ${slim-dest}
      tags:
        - ${slim-tag}
      username:
        from_secret: DOCKER_USERNAME
      password:
        from_secret: DOCKER_PASSWORD
  - name: jre
    image: plugins/docker
    settings:
      repo: djcass44/adoptopenjdk-spring-base
      dockerfile: ${jre-dest}
      tags:
        - ${jre-tag}
      username:
        from_secret: DOCKER_USERNAME
      password:
        from_secret: DOCKER_PASSWORD
trigger:
  when:
    event: push
"""


def export_build(jdk, distro):
    version = f"{jdk}-{distro}"
    data = build.replace("${version}", version)

    subtypes = versions[distro]
    for s in subtypes:
        data = data.replace(f"${{{s}-dest}}", f"{jdk}/{distro}/{s}/Dockerfile")
        data = data.replace(f"${{{s}-tag}}", s)
    with open(".drone.yml", "a") as f:
        f.write(data)


cleanup = 'rm -rf '

for x in range(0, len(jdks)):
    cleanup += f" {jdks[x]}*"

cleanup += ' .drone.yml'
print(f"Running cleanup: '{cleanup}'")
# remove generated files
res = subprocess.check_output(cleanup, shell=True)
for line in res.splitlines():
    print(line)

# create Dockerfiles
for j in range(0, len(jdks)):
    jdk = jdks[j]
    for d in range(0, len(distros)):
        distro = distros[d]
        distro_versions = versions[distro]
        print(f"{jdk}/{distro}: {distro_versions}")
        # make the base dockerfile
        dockerfile = dockerfiles[distro]
        dockerfile = dockerfile.replace("${version}", f"adoptopenjdk/openjdk{jdk}:{distro}")
        filename = f"{jdk}/{distro}/Dockerfile"
        dir_and_write(filename, dockerfile)
        export_build(jdk, distro)
        # make the subtypes (e.g. jre, slim)
        for v in range(0, len(distro_versions)):
            version = distro_versions[v]
            dockerfile = dockerfiles[distro]
            dockerfile = dockerfile.replace("${version}", f"adoptopenjdk/openjdk{jdk}:{distro}-{version}")
            filename = f"{jdk}/{distro}/{version}/Dockerfile"
            dir_and_write(filename, dockerfile)
            # export_build(f"{jdk}-{distro}-{version}", filename)
