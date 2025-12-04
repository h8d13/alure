# Maintainer: HADEON <hadean-eon-dev@proton.me>
pkgname=alure
pkgver=0.1.0
pkgrel=1
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
45958b76173b53072df39756635e1695e651e8c55ab8e5f565781d85ae8b1945c0f71784dfc3094ac8ed70ff4f0828f9bfaf1f00d2a7858b13fde8ce61b604d8  alure-master.tar.gz
"
