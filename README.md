# alure

## Install build tools

```
apk add alpine-sdk

# Key components:
# - abuild: builds packages from APKBUILD
# - apk: package manager
# - abuild-keygen: generates signing keys
```

## Create a package
## Browse community packages

## Install a communnity package

```
cd packages/$1
abuild -r

# install.sh - Install built package
#!/bin/sh
apk add --allow-untrusted ~/packages/x86_64/$1-*.apk
```
