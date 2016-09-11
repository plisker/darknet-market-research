#!/bin/bash

# Copy all text files in the Scripts folders in all the folders in this directory to the folders created with the copy_folders.sh file

currentdir="$PWD"

for f in "$currentdir"/*;
do
	a=${f##*/}
	cp "$f"/Scripts/*.txt ../copy-to-db/"$a"
done