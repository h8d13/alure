#!/bin/sh
# Preview package info

line="$1"

# Strip marker [*] or [ ]
line=$(echo "$line" | sed 's/^\[.\] //')

# Get package name (first field)
pkg=$(echo "$line" | awk '{print $1}')

# Strip version: remove everything after first dash followed by digit
pkg=$(echo "$pkg" | sed 's/-[0-9].*//')

# Query package info
apk query "$pkg" 2>&1
