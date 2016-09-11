#!/bin/bash

# Use this to create empty folders with all the names of the folders in this directory in some other directory

currentdir="$PWD"

for f in "$currentdir"/*;
do
	a=${f##*/}
	cd ../copy-to-db && mkdir "$a" 
done