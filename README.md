# alure

A walk or passage; -- applied to passages of various kinds.

> *The sides of every street were covered with fresh alures of marble.*
> T. Warton.

---

`Alure` is a helper for both `apk` and `flatpak` using `fzf` and `python` nder the hood. 

## Setup

### Run directly in python

`git clone git@gitlab.alpinelinux.org:h8d13/alure.git`

`python alure help`

### Install globally with apk

`git clone -b aports git@gitlab.alpinelinux.org:h8d13/alure.git`
`abuild -r`
`doas apk add --allow-untrusted ~/packages/user/arch/alure-x.x.x-rx.apk`

---

## Building

Code in `master` or seperate branch. Then use aports to ship.
Removing cached files `rm -rf /var/cache/distfiles/*`
