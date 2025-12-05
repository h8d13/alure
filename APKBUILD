# Maintainer: HADEON <hadean-eon-dev@proton.me>
pkgname=alure
pkgver=0.1.1
pkgrel=3
pkgdesc="Package manager using fzf and python3"
url="https://gitlab.alpinelinux.org/h8d13/alure"
arch="noarch"
license="MIT"
depends="python3 fzf"
makedepends=""
source="$pkgname-master.tar.gz::https://gitlab.alpinelinux.org/h8d13/alure/-/archive/master/alure-master.tar.gz"
builddir="$srcdir/alure-master"
options="!check"

build() {
    return 0
}

package() {
    cd "$builddir"

    # Install main executable
    install -Dm755 fzf-apk/alure-pm/alure "$pkgdir/usr/bin/alure"

    # Install helper scripts
    install -Dm755 fzf-apk/alure-pm/preview-deps.sh "$pkgdir/usr/lib/alure/preview-deps.sh"
    install -Dm755 fzf-apk/alure-pm/preview-info.sh "$pkgdir/usr/lib/alure/preview-info.sh"
}

sha512sums="
6acdb2581248096768c554458c4f2289a9f513b6f2f9e10d4affcd30a7479b0c2aba87938ab3f0396a8db5491c423983c2119eba0c0300ddedb5beb6aa922084  alure-master.tar.gz
"
