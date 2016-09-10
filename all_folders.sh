#!/bin/bash

# Place this file in the dnmarchives folder to run successfully
# Works assuming the scripts folder has already been copied into each extracted folder

currentdir="$PWD"

for f in "$currentdir"/*;
do
	cd "$f/scripts" && ./iterate_photos.sh
done;
