#!/bin/sh
# run flatpak app wrap 
[ -z "$1" ] && { echo "Usage: fp run <appname>"; exit 1; }
app=$(flatpak list --app --columns=application | grep -i "$1" | head -1)
[ -z "$app" ] && { echo "No app matching '$1' found"; exit 1; }
flatpak run "$app"
