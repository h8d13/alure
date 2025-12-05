#!/bin/sh
# Preview package info

line="$1"

# Strip ANSI codes first
line=$(echo "$line" | sed 's/\x1b\[[0-9;]*m//g')

# Get field 1 (marker + package), strip marker (• or space at start)
pkg_field=$(echo "$line" | cut -f1 | sed 's/^[• ] *//')

# Get package name (first word)
pkg=$(echo "$pkg_field" | awk '{print $1}')

# Strip version
pkg=$(echo "$pkg" | sed 's/-[0-9].*//')

# Query package info
apk query "$pkg" 2>&1
