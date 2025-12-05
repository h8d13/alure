# Maintainer: HADEON <hadean-eon-dev@proton.me>
pkgname=alure
pkgver=0.1.1
pkgrel=2
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
78d2e673f9baa56ebf48b57ca238188dc0ee89157c65ae3d8dfded8ed2d60fcf96510f108fc72400a4609156cec77bba1966c2c4d5c31ca06438cbd6a92b8efb  alure-master.tar.gz
"
