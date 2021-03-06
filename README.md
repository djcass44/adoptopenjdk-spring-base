# AdoptOpenJdk Spring Base

This repository contains the recipe for creating a number of slightly customised AdoptOpenJdk Java images.

## Supported tags

#### Releases

**Alpine**

* Java 11 - HotSpot - Alpine `11-alpine-jre`
* Java 11 - OpenJ9 - Alpine `11-j9-alpine-jre`
* Java 12 - HotSpot - Alpine `12-alpine-jre`
* Java 12 - OpenJ9 - Alpine `12-j9-alpine-jre`
* Java 13 - HotSpot - Alpine `13-alpine-jre`
* Java 13 - OpenJ9 - Alpine `13-j9-alpine-jre`
* Java 14 - HotSpot - Alpine `14-alpine-jre`
* Java 14 - OpenJ9 - Alpine `14-openj9-alpine-jre`

To use a non-JRE version (JDK), replace `jre` with `slim`

**Debian**

* Java 11 - HotSpot - Debian `11-debian-jre`
* Java 11 - OpenJ9 - Debian `11-j9-debian-jre`
* Java 12 - HotSpot - Debian `12-debian-jre`
* Java 12 - OpenJ9 - Debian `12-j9-debian-jre`
* Java 13 - HotSpot - Debian `13-debian-jre`
* Java 13 - OpenJ9 - Debian `13-j9-debian-jre`
* Java 14 - HotSpot - Debian `14-debian-jre`
* Java 14 - OpenJ9 - Debian `14-j9-debian-jre`

To use a non-JRE version (JDK), replace `jre` with `slim`

Current customisations:

* Adds `tomcat-native`
* Updates packages to latest stable versions

### Where are the images?

Images are dynamically generated by `setup.py`.

Creating images

```bash
python setup.py
```