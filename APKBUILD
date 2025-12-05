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
source="$pkgname-master.tar.gz:https://gitlab.alpinelinux.org/h8d13/alure/-/archive/master/alure-master.tar.gz?ref_type=heads&path=fzf-apk"
builddir="$srcdir/fzf-apk/alure-pm"
options="!check"

prepare() {
    # Unpack and strip the top-level directory
    cd "$srcdir"
    tar -xf "$srcdir/$pkgname-master.tar.gz" --strip-components=2
}

build() {
    return 0
}

package() {
    cd "$builddir"

    # Install main executable
    install -Dm755 alure "$pkgdir/usr/bin/alure"

    # Install helper scripts
    install -Dm755 preview-deps.sh "$pkgdir/usr/lib/alure/preview-deps.sh"
    install -Dm755 preview-info.sh "$pkgdir/usr/lib/alure/preview-info.sh"
}
