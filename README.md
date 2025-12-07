# alure

A walk or passage; -- applied to passages of various kinds.

> *The sides of every street were covered with fresh alures of marble.*
> T. Warton.

---

`Alure` is a helper for both `apk` and `flatpak` using `fzf` and `python` under the hood. 

It wraps common package operations behind a fuzzy search interface. Enabling you can search, inspect, and manage packages without remembering exact names or all the commands of APK/Flatpak.

## Setup

### Get the source code directly

```sh
wget https://gitlab.alpinelinux.org/h8d13/alure/-/archive/master/alure-master.tar.gz
tar xzf alure-master.tar.gz
cd alure-master
python alure help
```

### Run directly in python

```sh
git clone git@gitlab.alpinelinux.org:h8d13/alure.git
cd alure
python alure help
```

### Install globally with apk

```sh
git clone -b aports git@gitlab.alpinelinux.org:h8d13/alure.git
abuild -r
doas apk add --allow-untrusted ~/packages/user/arch/alure-x.x.x-rx.apk
```

---

## Building

Code in `master` or seperate branch. Then use branch `aports` to ship.
Removing cached files `rm -rf /var/cache/distfiles/*`
