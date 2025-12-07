#!/bin/sh
# Package extraction and preview utilities

# Extract clean package name (strips ANSI, markers, and version)
extract_package_name() {
    line="$1"
    # Strip ANSI codes
    line=$(echo "$line" | sed 's/\x1b\[[0-9;]*m//g')
    # Remove marker (• or space at start)
    line=$(echo "$line" | sed 's/^[• ] *//')
    # Get first field/word (package name with version)
    pkg=$(echo "$line" | awk '{print $1}')
    # Strip version
    pkg=$(echo "$pkg" | sed 's/-[0-9].*//')
    echo "$pkg"
}

# Extract app ID from flatpak line (field 2)
extract_app_id() {
    line="$1"
    echo "$line" | cut -f2
}

# Show package info (default action)
show_package_info() {
    line="$1"
    # Get field 1 (marker + package), strip marker (• or space at start)
    pkg_field=$(echo "$line" | cut -f1 | sed 's/^[• ] *//')
    # Get package name (first word)
    pkg=$(echo "$pkg_field" | awk '{print $1}')
    # Strip version
    pkg=$(echo "$pkg" | sed 's/-[0-9].*//')
    # Query package info
    apk query "$pkg" 2>&1
}

# Show flatpak dependencies
show_flatpak_deps() {
    line="$1"
    # Get field 2 (app ID)
    app_id=$(echo "$line" | cut -f2)
    # Get runtime and related info
    output=$(flatpak remote-info flathub "$app_id" 2>/dev/null | grep -E "Runtime|SDK|Subject|Extensions" | sed 's/^[[:space:]]*//')
    if [ -z "$output" ]; then
        echo "No dependency information available"
    else
        echo "$output"
    fi
}

# Main execution
case "${2:-info}" in
    extract-name)
        # Extract and output package name without newline
        extract_package_name "$1" | tr -d '\n'
        ;;
    extract-appid)
        # Extract and output app ID without newline
        extract_app_id "$1" | tr -d '\n'
        ;;
    flatpak-deps)
        # Show flatpak dependencies
        show_flatpak_deps "$1"
        ;;
    info|*)
        # Show package info (default)
        show_package_info "$1"
        ;;
esac
