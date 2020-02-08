#!/bin/bash

for folder in $(ls | grep -v '.sh' | sort -r); do
	echo "Destroying $folder ..."
	cd $folder
	../terraform.sh destroy --force
	cd ..
done

