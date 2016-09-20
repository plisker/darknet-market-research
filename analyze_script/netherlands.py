import csv
import numpy as np
import re
import os
from shutil import copyfile

def write_data_csv(data):
	#latitude, longitude
	with open('netherlands/netherlands.csv', 'w') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(data)

def netherland(path, archive):
	with open(path) as f:
		data = f.readlines()

	coordinates = []

	p = re.compile(ur'..(.*)')

	for i in range(len(data)):
		data[i] = eval(data[i])
		x, y = data[i]
		lat, lon = y
		if lat > 50 and lat < 54 and lon > 3 and lon < 6: 
			match = re.search(p, x)
			photo = match.group(1)
			coordinates.append(archive+"_geo"+photo)

	return coordinates

rootdir = "/Users/Paul/Dropbox/School/Harvard/Semester 5/CS 105- Privacy and Technology/Final Project/Data"
copy_destination = "/Users/Paul/Dropbox/darknet-market-research/analyze_script/netherlands/"

nl = []

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
		if file.endswith("coordinates_raw_data.txt"):
			archive = os.path.basename(subdir)
			path = os.path.join(subdir, file)

			nl_photos = netherland(path, archive)
			if len(nl_photos) > 0:
				for i in nl_photos:
					nl.append(i)

nl.sort()
for i in nl:
	file = rootdir+"/"+i
	p = re.compile(ur'.*\/(.*)')
 	match = re.search(p, file)
 	photo = match.group(1)
	
	dest = copy_destination+photo
	try:
		copyfile(file, dest)
	except:
		pass

# write_data_csv(nl)

