#!/usr/bin/env bash

# cleanup
rm .drone.yml || true
rm -rf 11* 12* 13*

declare -a StringArray=(
    "adoptopenjdk/openjdk11:alpine-jre 11-alpine-jre 11/jre/alpine/Dockerfile.hotspot.releases.full"
    "adoptopenjdk/openjdk11-openj9:alpine-jre 11-j9-alpine-jre 11/jre/alpine/Dockerfile.openj9.releases.full"
    "adoptopenjdk/openjdk12:alpine-jre 12-alpine-jre 12/jre/alpine/Dockerfile.hotspot.releases.full"
    "adoptopenjdk/openjdk12-openj9:alpine-jre 12-j9-alpine-jre 12/jre/alpine/Dockerfile.openj9.releases.full"
    "adoptopenjdk/openjdk13:alpine-jre 13-alpine-jre 13/jre/alpine/Dockerfile.hotspot.releases.full"
    "adoptopenjdk/openjdk13-openj9:alpine-jre 13-j9-alpine-jre 13/jre/alpine/Dockerfile.openj9.releases.full"
)

for val in "${StringArray[@]}"; do
    ./create.sh $val
done