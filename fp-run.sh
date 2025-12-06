#!/bin/bash
[ -z "$1" ] && { echo "Usage: fp <appname>"; exit 1; }
flatpak run "$(flatpak list --app --columns=application | grep -i "$1" | head -1)"

# usually some apps need for electron app certs 
# p11-kit p11-kit-server p11-kit-trust nss-tools
# doas update-ca-certificates
