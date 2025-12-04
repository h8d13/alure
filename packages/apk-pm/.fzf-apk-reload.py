#!/usr/bin/env python3
import sys
from pathlib import Path

query = sys.argv[1] if len(sys.argv) > 1 else ""

cache_file = Path("/home/hadean/.cache/fzf-apk/packages.cache")
installed = {'libltdl', 'lilv-libs', 'kmod-bash-completion', 'json-c', 'libncursesw', 'openrc-user', 'python3', 'ufw-bash-completion', 'uchardet-libs', 'glib', 'libvpx', 'nano', 'usbutils', 'abseil-cpp-raw-logging-internal', 'py3-cryptography', 'zimg', 'openssh-server', 'exo', 'polkit-elogind', 'libattr', 'yt-dlp-zsh-completion', 'libndp', 'libnftnl', 'opus', 'sqlite-libs', 'fontconfig', 'nghttp3', 'libice', 'libxcursor', 'logger', 'intel-ucode', 'lsblk', 'libxpresent', 'linux-firmware-hp', 'mkfontscale', 'coreutils', 'libliftoff', 'e2fsprogs-extra', 'libatk', 'sway-wallpapers', 'libidn2', 'swayidle-openrc', 'libatk-bridge', 'perl-error', 'libxcb', 'gdk-pixbuf', 'losetup', 'eudev-libs', 'libepoxy', 'desktop-file-utils', 'yt-dlp', 'libatomic', 'mesa-gbm', 'i3status', 'mesa-gles', 'libfontenc', 'py3-brotli', 'runuser', 'wl-clipboard-bash-completion', 'at-spi2-core-libs', 'freetype', 'libxkbfile', 'libcrypto3', 'openrc-bash-completion', 'speexdsp', 'libuuid', 'libtheora', 'nettle', 'zix-libs', 'fzf-zsh-plugin', 'json-glib', 'xorg-server-common', 'openssh-server-common-openrc', 'pango', 'libblkid', 'util-linux-login', 'clutter-gtk', 'git-doc', 'adwaita-icon-theme', 'libxinerama', 'vulkan-loader', 'libjpeg-turbo', 'ffmpeg7-libavcodec', 'libxdmcp', 'glslang-libs', 'dbus-libs', 'icu-libs', 'mesa-egl', 'pyc', 'networkmanager-bash-completion', 'libvdpau', 'cfdisk', 'libxv', 'yaml', 'util-linux-openrc', 'alsa-lib', 'libxfce4util', 'llvm21-libs', 'libhwy', 'lscpu', 'less-doc', 'sord-libs', 'libx86emu', 'ca-certificates', 'bash', 'ffmpeg-libavfilter', 'musl-utils', 'git-zsh-completion', 'yt-dlp-bash-completion', 'openrc-init', 'libxrandr', 'libcamera-ipa', 'xkeyboard-config', 'pciutils', 'jansson', 'wpa_supplicant', 'py3-cffi', 'wl-clipboard', 'lame-libs', 'shared-mime-info', 'alsa-ucm-conf', 'ffmpeg7-libavutil', 'bridge', 'libssl3', 'git-perl', 'libplacebo', 'libpng', 'gmp', 'apk-tools', 'lddtree', 'skalibs-libs', 'sway-zsh-completion', 'libxcvt', 'p11-kit', 'thunar', 'foot', 'intel-media-driver', 'alpine-baselayout-data', 'utf8proc', 'libdvdnav', 'alsa-utils-udev', 'hwinfo', 'py3-mutagen', 'yt-dlp-ejs-pyc', 'elogind-bash-completion', 'coreutils-env', 'libevent', 'libdisplay-info', 'mtdev', 'curl-zsh-completion', 'libpulse', 'libevdev', 'dmesg', 'pcre2', 'alsa-utils', 'e2fsprogs', 'readline', 'curl', 'libintl', 'libnotify', 'brotli-libs', 'dbus-daemon-launch-helper', 'mount', 'partx', 'linux-firmware-i915', 'x264-libs', 'swayidle', 'acpid-openrc', 'libapk', 'cogl', 'python3-pycache-pyc0', 'acpid', 'apk-tools-zsh-completion', 'libelogind', 'bash-completion', 'numactl', 'zlib', 'zram-init', 'yt-dlp-core', 'fd-zsh-completion', 'ffmpeg-libavformat', 'grub-bash-completion', 'kbd-bkeymaps', 'font-unifont', 'deno-bash-completion', 'pkgconf', 'c-ares', 'foot-bash-completion', 'kmod-zsh-completion', 'py3-cparser-pyc', 'util-linux-bash-completion', 'uuidgen', 'libarchive', 'xcb-util-wm', 'libcap-ng', 'libpanelw', 'libusb', 'pciutils-libs', 'ifupdown-ng', 'py3-cparser', 'wpa_supplicant-openrc', 'sndio-libs', 'ncurses-terminfo-base', 'setpriv', 'libdav1d', 'libxfont2', 'grub', 'sway-bash-completion', 'libwebp', 'libcdio-paranoia', 'py3-secretstorage-pyc', 'mpv', 'ffmpeg', 'fribidi', 'libjxl', 'zstd-libs', 'cups-libs', 'udev-init-scripts-openrc', 'jack', 'glib-bash-completion', 'mesa-gl', 'libxshmfence', 'util-linux-misc', 'busctl', 'py3-cffi-pyc', 'ncurses-terminfo', 'libxvmc', 'simdutf', 'alpine-conf', 'fftw-double-libs', 'libdvdread', 'umount', 'wayland-libs-egl', 'libxft', 'mandoc', 'wl-clipboard-zsh-completion', 'utmps-libs', 'openssh', 'openssh-server-common', 'libuv', 'man-pages', 'openrc', 'x265-libs', 'orc', 'fftw-single-libs', 'xwayland', 'foot-openrc', 'libvorbis', 'liblastlog2', 'nss', 'wipefs', 'libcurl', 'openssh-client-default', 'device-mapper-libs', 'libdrm', 'mpdecimal', 'confuse', 'rav1e-libs', 'mandoc-apropos', 'attr', 'cairo', 'xfconf', 'swaylock', 'ca-certificates-bundle', 'libxcomposite', 'python3-pyc', 'libtasn1', 'v4l-utils-libs', 'libunibreak', 'libxtst', 'clutter', 'firefox', 'libopenmpt', 'lcms2', 'duktape-libs', 'xcb-util-renderutil', 'wayland-libs-client', 'xf86-video-intel', 'dosfstools', 'findmnt', 'iptables-openrc', 'swaylock-openrc', 'hwdata-usb', 'libcamera', 'libbsd', 'coreutils-sha512sum', 'libsm', 'flock', 'busybox-mdev-openrc', 'libeconf', 'libseat', 'linux-lts', 'openssh-client-common', 'libstdc++', 'spirv-tools', 'mesa-va-gallium', 'libinput-libs', 'mpv-bash-completion', 'wayland-libs-server', 'ufw-pyc', 'elogind-common', 'tdb-libs', 'fd-bash-completion', 'sway-openrc', 'pcsc-lite-libs', 'libgomp', 'dialog', 'sof-firmware', 'bottom-bash-completion', 'libsmartcols', 'yt-dlp-ejs', 'libxrender', 'bottom-zsh-completion', 'eudev-openrc', 'hicolor-icon-theme', 'musl', 'linux-firmware-dell', 'dbus', 'xkbcomp', 'abseil-cpp-strings', 'gobject-introspection', 'xcb-util', 'busybox-openrc', 'nspr', 'libxext', 'py3-jeepney-pyc', 'kbd', 'librist', 'vidstab', 'alsaconf', 'cairo-gobject', 'ufw', 'libsndfile', 'librsvg', 'libpciaccess', 'less', 'font-dejavu', 'lshw', 'yt-dlp-core-pyc', 'libtirpc-nokrb', 'mesa-vulkan-layers', 'libSvtAv1Enc', 'swaylockd', 'libfdisk', 'libmd', 'gnome', 'libmnl', 'libgtop', 'elogind', 'brightnessctl-openrc', 'swaylock-bash-completion', 'libssh', 'apk-tools-bash-completion', 'umpv', 'shaderc', 'encodings', 'swaylock-zsh-completion', 'startup-notification', 'libxau', 'wmenu', 'mpv-zsh-completion', 'libxfixes', 'mdev-conf', 'libffi', 'ffmpeg-libavcodec', 'xz-libs', 'libbluray', 'ffmpeg-libswscale', 'mkinitfs', 'swayidle-bash-completion', 'gnutls', 'ffmpeg-libswresample', 'polkit-elogind-libs', 'py3-websockets-pyc', 'intel-gmmlib', 'libgnome-games-support', 'polkit-openrc', 'py3-brotli-pyc', 'sway', 'alpine-keys', 'gtk-update-icon-cache', 'libva', 'zsh', 'libinput-udev', 'libass', 'blkid', 'cryptsetup-libs', 'mbedtls', 'scudo-malloc', 'libwebpdemux', 'doas', 'py3-secretstorage', 'libvpl', 'gtk-layer-shell', 'kmod-libs', 'ssl_client', 'setarch', 'ufw-openrc', 'serd-libs', 'ffmpeg7-libswresample', 'wlroots', 'icu-data-en', 'brightnessctl', 'libmount', 'libxml2', 'libflac', 'acl-libs', 'gdbm', 'zram-init-zsh-completion', 'abseil-cpp-strings-internal', 'libcom_err', 'mcookie', 'fzf-bash-plugin', 'shadow', 'libasyncns', 'hwdata-pci', 'libcdio', 'sratom', 'elogind-openrc', 'webrtc-audio-processing', 'graphite2', 'fcft', 'git', 'swayidle-zsh-completion', 'kbd-misc', 'exo-libs', 'ffmpeg-libavdevice', 'perl', 'libsamplerate', 'yajl', 'avahi-libs', 'libsodium', 'libedit', 'perl-git', 'networkmanager-openrc', 'libx11', 'kmod', 'polkit-common', 'py3-pycryptodomex', 'scanelf', 'wget', 'linux-pam', 'git-bash-completion', 'tiff', 'libtirpc-conf', 'linux-firmware-intel', 'busybox-extras', 'gtk+3.0', 'libunwind', 'openssh-sftp-server', 'libexpat', 'zsh-vcs', 'grim', 'e2fsprogs-libs', 'git-init-template', 'agetty', 'libudfread', 'swaybg', 'xfconf-bash-completion', 'tar', 'libxdamage', 'mpg123-libs', 'yt-dlp-ejs-rt-deno', 'bottom', 'luajit', 'acpi', 'roc-toolkit-libs', 'py3-cryptography-pyc', 'libelf', 'libgee', 'elogind-zsh-completion', 'grub-efi', 'mesa-dri-gallium', 'mesa', 'hwinfo-libs', 'libsrt', 'libgcc', 'busybox-binsh', 'nghttp2-libs', 'hexdump', 'libnm', 'openssh-keygen', 'iptables', 'basu', 'rubberband-libs', 'libcap2', 'util-linux', 'coreutils-fmt', 'sfdisk', 'soxr', 'libxfce4panel', 'libxi', 'libunistring', 'libxtables', 'py3-mutagen-pyc', 'libbz2', 'lz4-libs', 'busybox', 'cjson', 'libva-intel-driver', 'libgudev', 'udev-init-scripts', 'linux-firmware-none', 'foot-zsh-completion', 'ifupdown-ng-wifi', 'libwebpmux', 'py3-jeepney', 'eudev', 'fzf', 'swaybg-openrc', 'alsa-utils-openrc', 'deno', 'at-spi2-core', 'micro', 'ffmpeg-libavutil', 'libmenuw', 'dbus-openrc', 'fstrim', 'libnl3', 'py3-websockets', 'libformw', 'harfbuzz', 'libsharpyuv', 'networkmanager', 'brightnessctl-udev', 'jemalloc', 'deno-zsh-completion', 'swaybar', 'libdvdcss', 'libxxf86vm', 'libxscrnsaver', 'libxfce4ui', 'libxkbcommon', 'alpine-baselayout', 'mesa-vulkan-intel', 'libdovi', 'libexif', 'libcaca', 'alpine-release', 'musl-locales', 'wayland-libs-cursor', 'libogg', 'libzmq', 'pixman', 'libpsl', 'networkmanager-wifi', 'agetty-openrc', 'linux-firmware-lenovo', 'swaynag', 'networkmanager-cli', 'zram-init-openrc', 'vulkan-tools', 'zstd', 'libsixel', 'linux-firmware-other', 'openrc-zsh-completion', 'fd', 'kbd-openrc', 'xvidcore', 'pipewire-libs', 'aom-libs'}

def strip_version(pkg):
    parts = pkg.split('-')
    for i, part in enumerate(parts):
        if part and part[0].isdigit():
            return '-'.join(parts[:i])
    return pkg

with open(cache_file) as f:
    lines = f.readlines()

marked = []
for line in lines:
    if not line.strip():
        continue
    pkg_name = strip_version(line.split()[0])
    marker = '[*]' if pkg_name in installed else '[ ]'
    marked.append(f"{marker} {line}")

if query:
    exact, prefix, contains, desc = [], [], [], []
    q = query.lower()
    
    for line in marked:
        pkg_part = line[4:]
        parts = pkg_part.split()
        if not parts:
            continue
        pkg_name = strip_version(parts[0]).lower()
        
        if pkg_name == q:
            exact.append(line)
        elif pkg_name.startswith(q):
            prefix.append(line)
        elif q in pkg_name:
            contains.append(line)
        elif q in pkg_part.lower():
            desc.append(line)
    
    marked = exact + prefix + contains + desc

for line in marked:
    print(line, end="")
