#!/usr/bin/env bash

# check argument length != 0
if [ $# -eq 0 ]
  then
    echo "ERROR: No arguments supplied! An image name is required"
    exit 1
fi
# check argument 1 is provided
if [ -z "$1" ]
  then
    echo "ERROR: Bad image"
    exit 1
fi
# check argument 2 is provided
if [ -z "$2" ]
  then
    echo "ERROR: Bad tag"
    exit 1
fi
# check argument 3 is provided
if [ -z "$3" ]
  then
    echo "ERROR: Bad destination"
    exit 1
fi

version="$1"
tag="$2"
dest="$3"

echo "Generating stub for image: ${version}"

mkdir -p "$(dirname "${dest}")" || exit
touch "${dest}"

echo "FROM ${version}
LABEL maintainer='Django Cass <django@dcas.dev>'

# update packages and install tomcat-native
RUN apk upgrade --no-cache -q && \\
    apk add --no-cache tomcat-native
" > ${dest}

echo "
---
kind: pipeline
name: ${version}

steps:
  - name: docker
    image: plugins/docker
    settings:
      repo: djcass44/adoptopenjdk-spring-base
      dockerfile: ${dest}
      tags:
        - ${tag}
      username:
        from_secret: DOCKER_USERNAME
      password:
        from_secret: DOCKER_PASSWORD
trigger:
  when:
    event: push
" >> .drone.yml