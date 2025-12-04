# Maintainer: HADEON <hadean-eon-dev@proton.me>
pkgname=alure
pkgver=0.1.1
pkgrel=0
pkgdesc="Package manager using fzf and python3"
url="https://gitlab.alpinelinux.org/h8d13/alure"
arch="noarch" 
license="MIT"
depends="python3 fzf"
makedepends=""
source="$pkgname-$pkgver.tar.gz::https://gitlab.alpinelinux.org/h8d13/alure/-/archive/v$pkgver/alure-v$pkgver.tar.gz"
builddir="$srcdir/$pkgname-v$pkgver"
options="!check"

build() {
    # Nothing to build for pure Python/shell scripts
    return 0
}

package() {
    cd "$builddir"
    
    # Install main executable
    install -Dm755 fzf-apk/alure-pm/alure "$pkgdir"/usr/bin/alure
    
    # Install helper scripts to a private lib directory (not in user's PATH)
    install -Dm755 fzf-apk/alure-pm/preview-deps.sh "$pkgdir"/usr/lib/alure/preview-deps.sh
    install -Dm755 fzf-apk/alure-pm/preview-info.sh "$pkgdir"/usr/lib/alure/preview-info.sh
    
    # Install documentation (should be seperate -doc pkg)
    #install -Dm644 README.md "$pkgdir"/usr/share/doc/$pkgname/README.md
    
    # Install license file
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

sha512sums="
cf8f222363d1c0d09bf796d002564cc952e6602e8b983d65ac6fde760b4d1c62aac457de7d359dc51a307b3609445e1468c19ca0768dceb4e588898ad9b984b5  alure-0.1.1.tar.gz
"
