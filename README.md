# AdoptOpenJdk Spring Base

This repository contains the recipe for creating a number of slightly customised AdoptOpenJdk Java images.

Current customisations:

* Adds `tomcat-native`
* Updates packages to latest stable versions

### Where are the images?

Images are dynamically generated by `create.sh` and `setup.sh`.

Creating images

```bash
./setup.sh
```