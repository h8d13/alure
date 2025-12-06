# Maintainer: HADEON <hadean-eon-dev@proton.me>
pkgname=alure
pkgver=0.1.2
pkgrel=1
pkgdesc="Package manager using fzf and python3"
url="https://gitlab.alpinelinux.org/h8d13/alure"
arch="noarch"
license="MIT"
depends="python3 fzf"
makedepends=""
source="https://gitlab.alpinelinux.org/h8d13/alure/-/archive/master/alure-master.tar.gz"
builddir="$srcdir/alure-master"
options="!check"

prepare() {
    default_prepare
}

build() {
    return 0
}

package() {
    cd "$builddir"
    install -Dm755 alure "$pkgdir/usr/bin/alure"
    install -Dm755 preview-deps.sh "$pkgdir/usr/lib/alure/preview-deps.sh"
    install -Dm755 preview-info.sh "$pkgdir/usr/lib/alure/preview-info.sh"
}
sha512sums="SKIP"
