FROM adoptopenjdk/openjdk13:alpine
LABEL maintainer='Django Cass <django@dcas.dev>'

# update packages and install tomcat-native
RUN apk upgrade --no-cache -q && \
    apk add --no-cache tomcat-native
    