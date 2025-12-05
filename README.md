# alure

> A walk or passage; -- applied to passages of various kinds.
> *The sides of every street were covered with fresh alures of marble.*
> T. Warton.

---

## Install build tools

```
apk add alpine-sdk
# Key components:
# - abuild: builds packages from APKBUILD
# - apk: package manager
# - abuild-keygen: generates signing keys
```

### Setup build

```
doas addgroup user abuild
abuild-keygen -a -i
```
> Or something along those lines.

## Useful for building

```
#reset
abuild clean cleanpkg cleancache
rm /var/cache/distfiles/alure-master.tar.gz
# push changes before
abuild checksum
abuild -r
# add and test
apk add --allow-untrusted alure-x.x.x-rx.apk
alure help
```

