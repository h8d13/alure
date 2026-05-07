# alure

A walk or passage; -- applied to passages of various kinds.

> *The sides of every street were covered with fresh alures of marble.*
> T. Warton.

---

`Alure` is a helper for both `apk` and `flatpak` using `fzf` and `python` under the hood. 

It wraps common package operations behind a fuzzy search interface. Enabling you can search, inspect, and manage packages without remembering exact names or all the commands of APK/Flatpak.

## Setup

### Run directly in python

```sh
git clone <url>
cd alure
python alure help
```

### From source

```sh
git clone <url>
cd alure
abuild -r
doas apk add ~/packages/user/arch/alure-x.x.x-rx.apk
# adapt path
```
---

