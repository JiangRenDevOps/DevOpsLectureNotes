#!/bin/bash
set -e

for folder in $(ls | grep -v '.sh' | sort -r); do
	echo "Destroying $folder ..."
	cd $folder
	../terraform.sh destroy --force
	sudo rm -rf .terraform
	cd ..
done

echo Please remove the S3 bucket (s3-terraform-state-storage-*) that stores terraform state.
