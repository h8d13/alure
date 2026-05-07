# Maintainer: HADEON <hadean-eon-dev@proton.me>
pkgname=alure
pkgver=0.1.4
pkgrel=0
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
    install -Dm755 preview-hist.sh "$pkgdir/usr/lib/alure/preview-hist.sh"
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 README.md "$pkgdir/usr/share/doc/$pkgname/README.md"
}
sha512sums="
6e9c0ad28639c64e90261d45d3383684c034e8a18ba47294cf3be63849763019555c4d0573fde5b968f299f7aa40b321925ad05b6dc8c1a69f3dd1e1e0bcc1e6  alure-master.tar.gz
"
