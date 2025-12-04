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
ad722151068627a53f09805624e685fb5a15bc39e884a05e4bc540b3a92a8d8afa56e2841ca9a54fca7f114e39370b4d814d2dd7a0be33fa281fb46a660cdd6c  alure-master.tar.gz
"
