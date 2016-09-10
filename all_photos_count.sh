#!/bin/bash

# Place this file in the Final Project/Paper for Publication folder to run
# Outputs a count of total images measured by the number of lines in each archive's all_photos.txt file

currentdir="$PWD"

for f in "$currentdir"/*;
do
	cd "$f" &&
	echo -n "${PWD##*/} " >> ../all_photos_count.txt &&
	wc -l all_photos.txt >> ../all_photos_count.txt
done;
