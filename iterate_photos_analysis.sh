#!/bin/bash

currentdir="$PWD"

for f in "$currentdir"/*;
do
	cd "$f" && python /Users/Paul/Dropbox/darknet-market-research/analyze_script/analysis.py
done;