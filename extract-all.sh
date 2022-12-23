#!/bin/bash

delete=false

while getopts d flag
do
    case "${flag}" in
        d) delete=true;;
    esac
done

echo $delete

shopt -s globstar
for f in **/*.rar; do
    extractFolder="${f%.*}"
    mkdir $extractFolder

    unrar e -o- "$f" $extractFolder

    if [ $? -eq 0 ]; then
        echo 'success'
        if [ $delete = true ]; then
            find $(dirname $f) -maxdepth 1 -type f -delete
        fi
    fi

done
