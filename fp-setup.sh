#!/bin/sh
# flatpak setup script

# check and install flatpak and cert tools
if ! command -v flatpak >/dev/null 2>&1; then
    echo "Installing flatpak and cert tools..."
    doas apk add flatpak p11-kit p11-kit-server p11-kit-trust nss-tools
    doas update-ca-certificates
fi

# add flathub repo
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

echo "Flatpak setup complete"
