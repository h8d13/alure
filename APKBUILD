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
source="https://gitlab.alpinelinux.org/h8d13/alure/-/archive/master/alure-master.tar.gz"
builddir="$srcdir/alure-master/fzf-apk/alure-pm"
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
sha512sums="
28f46637523c40ae16ec02d89731bca4ff4afdf5b9fe9cb5fd074d097d639984ea0ab5e4d87cad5b48cabe945f7cb851d62985f33a1593ea17065074796874b4  alure-master.tar.gz
"
