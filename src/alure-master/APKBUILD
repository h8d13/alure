# Maintainer: HADEON <hadean-eon-dev@proton.me>
pkgname=alure
pkgver=0.1.0
pkgrel=0
pkgdesc="Package manager using fzf and python3"
url="https://gitlab.alpinelinux.org/h8d13/alure"
arch="noarch" 
license="MIT"
depends="python3 fzf"
makedepends=""
source="https://gitlab.alpinelinux.org/h8d13/alure/-/archive/master/alure-master.tar.gz"
builddir="$srcdir/$pkgname-master"
options="!check"

build() {
    # Nothing to build for pure Python/shell scripts
    return 0
}

package() {
    cd "$builddir"
    
    # Install main executable
    install -Dm755 alure-pm/fzf-apk/alure "$pkgdir"/usr/bin/alure
    # Install helpers
    install -Dm755 alure-pm/fzf-apk/preview-deps.sh "$pkgdir"/usr/bin/preview-deps.sh
    install -Dm755 alure-pm/fzf-apk/preview-info.sh "$pkgdir"/usr/bin/preview-info.sh
    
    # Optional: Install documentation
    install -Dm644 README.md "$pkgdir"/usr/share/doc/$pkgname/README.md
    
    # Optional: Install license file
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

sha512sums="
6956bf45a2ae41db9c6f4db680929969a0d406dfb77e016f0641df4da2c7d76adc6944ddcbbd9c0368090fd47565eaa602d42073c483c71fc53a44a5a9bf1f67  alure-master.tar.gz
"
