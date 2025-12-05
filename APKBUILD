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
20e5b1f74ea969f2cc5c372fa56ed1efca4185508616334087fb4e0b0b880854f4251f0f5808195c42899149f809bdd438bf808b67296bc5ff26f0b341e46182  alure-master.tar.gz
"
