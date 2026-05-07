#!/bin/sh

cleanup() {
	rm -rf src tmp pkg
	rm /var/cache/distfiles/alure-master.tar.gz  
}

cleanup
abuild checksum
abuild -r
