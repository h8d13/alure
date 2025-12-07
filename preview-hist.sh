#!/bin/bash
# APK History Viewer: -l N (last N) | -f N (first N) | no args (all)

LOG_FILE="/var/log/apk.log"
[[ ! -f "$LOG_FILE" ]] && { echo "Error: $LOG_FILE not found" >&2; exit 1; }

case "$1" in
    -l) [[ "$2" =~ ^[0-9]+$ ]] && tail -n "$2" "$LOG_FILE" | less || { echo "Error: Invalid count" >&2; exit 1; } ;;
    -f) [[ "$2" =~ ^[0-9]+$ ]] && head -n "$2" "$LOG_FILE" | less || { echo "Error: Invalid count" >&2; exit 1; } ;;
    -h|--help) echo "Usage: $0 [-l N | -f N]"; exit 0 ;;
    "") less "$LOG_FILE" ;;
    *) echo "Error: Unknown option: $1" >&2; exit 1 ;;
esac
