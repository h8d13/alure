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

## Useful for building

```
rm /var/cache/distfiles/alure-master.tar.gz
abuild checksum
abuild -r
apk add --allow-untrusted ~/packages/x86_64/$1-*.apk
apk add --allow-untrusted ~/packages/user/x86_64/alure-0.1.0-r0.apk
alure help
```
