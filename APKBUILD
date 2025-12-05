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
49ae147c54fd66d6e2584acb95bedd322a2a7147b8c1ea80d71fa637027712786ad4306e6c6e4a23fb5c89fab1ff1fe28116e37f282ce172b7e6b1cf958e0d1b  alure-master.tar.gz
"
