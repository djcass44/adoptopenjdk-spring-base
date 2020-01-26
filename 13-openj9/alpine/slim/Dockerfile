FROM adoptopenjdk/openjdk13-openj9:alpine-slim
LABEL maintainer='Django Cass <django@dcas.dev>'

# update packages and install tomcat-native
RUN apk upgrade --no-cache -q && \
    apk add --no-cache tomcat-native
    