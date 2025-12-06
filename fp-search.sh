#!/bin/sh
# fzf search for flatpak apps

# check flatpak is installed
if ! command -v flatpak >/dev/null 2>&1; then
    echo "flatpak not found. Run: alure fp setup"
    exit 1
fi

# check fzf is installed
if ! command -v fzf >/dev/null 2>&1; then
    echo "fzf not found"
    exit 1
fi

search_apps() {
    query="$1"

    # get installed apps for marking
    installed=$(flatpak list --app --columns=application)

    # search flathub
    selection=$(flatpak remote-ls flathub --app --columns=name,application,description | \
    while IFS=$'\t' read -r name app desc; do
        if echo "$installed" | grep -q "^$app$"; then
            printf "• %s\t%s\t%s\n" "$name" "$app" "$desc"
        else
            printf "  %s\t%s\t%s\n" "$name" "$app" "$desc"
        fi
    done | fzf \
        --ansi \
        --border=rounded \
        --height=95% \
        --prompt="  Flatpak > " \
        --header="•:installed  ⏎:install/remove" \
        --preview='flatpak remote-info flathub $(echo {} | cut -f2) 2>/dev/null' \
        --preview-window='right:50%:border-left:wrap:~0' \
        --delimiter=$'\t' \
        --with-nth=1,3 \
        --query="$query")

    [ -z "$selection" ] && exit 0

    # extract app id and check if installed
    app_id=$(echo "$selection" | cut -f2)
    is_installed=$(echo "$selection" | grep -q '^•' && echo "yes" || echo "no")

    if [ "$is_installed" = "yes" ]; then
        echo "Removing: $app_id"
        flatpak uninstall -y "$app_id" && echo "Removed successfully"
    else
        echo "Installing: $app_id"
        flatpak install -y flathub "$app_id" && echo "Installed successfully"
    fi

    sleep 0.5
    search_apps "$query"
}

search_apps "$1"
