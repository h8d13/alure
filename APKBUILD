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
source="$pkgname-$pkgver.tar.gz::https://gitlab.alpinelinux.org/h8d13/alure/-/archive/master/alure-master.tar.gz"
builddir="$srcdir/$pkgname-master"
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
    
    # Install documentation
    install -Dm644 README.md "$pkgdir"/usr/share/doc/$pkgname/README.md
    
    # Install license file
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

sha512sums="
b30c1e2423f4d1a9f47466a065117dc33c0faf973accab61ac9ce8db08eda24903d526f64ef6b391c3cfce4765ecdc3dba966e4d660b07b1f1703f20a4a1c3e9  alure-0.1.0.tar.gz
"
