#!/bin/bash

currentdir="$PWD"

cd ../
name="${PWD##*/}"
cd ../
name+="_geo"

newpath="$PWD"
newpath+="/$name"

cd "$name"
temporary="this_is_a_temporary_folder"
mkdir "$temporary"
newpath+="/$temporary"


cd "$currentdir"

# Will pass tuples of photos with geotag, and filepath will be used to copy photos into a particular folder
while read p; do
	GET="$p"
	IFS="'" read _ b _ <<< "$GET"

	# Change according to folder to which photos should be copied. Folder must exist.
	gcp --parents "$b" "$newpath"
done <coordinates_raw_data.txt

cd "../../$name"
rmdir "$temporary"
cd "$currentdir"