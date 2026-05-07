#!/bin/sh
ARCH=$(apk --print-arch)

cleanup() {
	rm -rf src tmp pkg
	rm /var/cache/distfiles/alure-master.tar.gz  
	rm -f ~/packages/"$USER"/"$ARCH"/alure-*.apk # nuke glob
	
}


cleanup
abuild checksum
abuild -r

doas apk add --no-cache ~/packages/"$USER"/"$ARCH"/alure-*.apk # install
