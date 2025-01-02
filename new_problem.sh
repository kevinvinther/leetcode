#!/bin/bash

read -p "Problem number: " number
read -p "Problem name: " name

formatted_number=$(printf "%05d" $number)

formatted_name=$(echo "$name" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')

new_folder="${formatted_number}-${formatted_name}"

cp -r 00000-template "$new_folder"

echo "Template copied to $new_folder"
