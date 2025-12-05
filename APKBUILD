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
229a5ea47bfa5e66a035e3f443de5441d7ba94e7db606905b02abca5c45487afca1fcf00360e908ff3b17cb8b8eb2464f50337195525374a7abeb38b640f4a6c  alure-master.tar.gz
"
