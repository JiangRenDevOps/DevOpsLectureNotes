#!/bin/bash
set -e

for folder in $(ls | grep -v '.sh' | sort); do
	echo "Creating $folder ..."
	cd $folder
	../terraform.sh init
	../terraform.sh apply -auto-approve
	cd ..
done

