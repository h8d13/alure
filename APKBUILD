# Maintainer: HADEON <hadean-eon-dev@proton.me>
pkgname=alure
pkgver=0.1.1
pkgrel=4
pkgdesc="Package manager using fzf and python3"
url="https://gitlab.alpinelinux.org/h8d13/alure"
arch="noarch"
license="MIT"
depends="python3 fzf"
makedepends=""
source="alure
	preview-deps.sh
	preview-info.sh
	"
builddir="$srcdir"
options="!check"

prepare() {
    # Files are already in srcdir from source list
    return 0
}

build() {
    return 0
}

package() {
    cd "$builddir"
    install -Dm755 alure "$pkgdir/usr/bin/alure"
    install -Dm755 preview-deps.sh "$pkgdir/usr/lib/alure/preview-deps.sh"
    install -Dm755 preview-info.sh "$pkgdir/usr/lib/alure/preview-info.sh"
}
sha512sums="
23d31d71881bcedc25ce09a9bb84288513f0c8d6c1bbe1eba2e6730b9d2af31d63f0cda0d442969c5b16988e2604b4c4545e9109a241971ee234ba4945743718  alure
723b3327e2920b6396b7d9cca6c7da9afe9b4bbe735bae5d804645ae2051b8e8ae68ea1370b817e7f468ad06e50c856d9ce5447e889a4256311e32436bb9a9c7  preview-deps.sh
4540bed72f1a362418dea25de44212d2f538e2af24acc9b46eee44fe39bae9d9fc73fd24694d7ca567787bb71b992599f78700ed424dbe70996bacba1f318fe4  preview-info.sh
"
