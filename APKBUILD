# Maintainer: HADEON <hadean-eon-dev@proton.me>
pkgname=alure
pkgver=0.1.4
pkgrel=1
pkgdesc="Package manager using fzf and python3"
url="https://github.com/h8d13/alure"
arch="noarch"
license="MIT"
depends="python3 fzf"
makedepends=""
source="alure-master.tar.gz::https://github.com/h8d13/alure/archive/refs/heads/master.tar.gz"
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
97425777de57cae9948b90e91f2357b989aadd4b7d73fe2d7fa714e8b86d82164f0c5c50c750c6e2b4167608819bd759b90bd0afe09850ce216e63b4aa5110e9  alure-master.tar.gz
"
