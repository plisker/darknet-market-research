#!/bin/bash

# Will find all photos in directories starting at ../ and anything below, save filepath to all_photos.txt
find .. -type f -iname \*.jpg > all_photos.txt
find .. -type f -iname \*.jpeg >> all_photos.txt

# Will pass all the filepaths into the python2 script that outputs a tuple of filepath and coordinates
while read p; do
    python2 geodata.py "$p" >>coordinates_raw_data.txt
done <all_photos.txt

# Creates new folder with the same name as parent directory, but with "_geo" appended to end
currentdir="$PWD"

cd ../
name="${PWD##*/}"
cd ../
name+="_geo"

mkdir "$name"
newpath="$PWD"
newpath+="/$name"

cd "$currentdir"

# Will pass tuples of photos with geotag, and filepath will be used to copy photos into a particular folder
./copy.sh