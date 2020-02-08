#!/bin/bash
set -e 

function backend_config() {
    echo "key = \"$folder_name/terraform.tfstate\"" > $tmp_file

    cd "$(dirname "$0")/1.s3-state"
    terraform output | grep parameter | cut -d '=' -f 2- >> $tmp_file
    cd "$work_folder"
}

function terraform() {
    volumn_to_mount="-v ${script_folder}:/app -v $tmp_file:$tmp_file -v $HOME/.aws:/root/.aws -v $HOME/.ssh:/root/.ssh"
    current_folder_name="$(basename "$(pwd)")"
    docker run --rm -it -w /app/${current_folder_name} ${volumn_to_mount} hashicorp/terraform $@
    #docker run --entrypoint /bin/sh --rm -it -w /app/${current_folder_name} ${volumn_to_mount} hashicorp/terraform $@
}

# Generate backend parameter file
export script_folder="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
export folder_name="$(basename "$(pwd)")"
export work_folder="$(pwd)"

if [ "$folder_name" == "1.s3-state" ]; then
    terraform $@
    exit 0
fi

export tmp_file=~/.tmp.tfvars
backend_config
if [ "$1" == "init" ]; then
    terraform $@ -backend-config=$tmp_file -backend=true
else
    terraform $@
fi
