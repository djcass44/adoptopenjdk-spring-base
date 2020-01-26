FROM adoptopenjdk/openjdk11:debian-slim
LABEL maintainer='Django Cass <django@dcas.dev'

# update packages and install tomcat-native
RUN apt-get update &&     DEBIAN_FRONTEND=noninteractive apt-get install -yq libtcnative-1 &&     apt-get clean -y &&     apt-get autoclean -y &&     apt-get autoremove -y &&     rm -rf /var/lib/apt/lists/*
    