import csv
import numpy as np
import re
import os

def import_coordinates(file):
	with open(file) as f:
		data = f.readlines()

	coordinates = set()

	for i in range(len(data)):
		data[i] = eval(data[i])
		x, y = data[i]
		coordinates.add(y)

	return coordinates
	
def import_all_photos(file):
	with open(file) as f:
		data = f.readlines()

	photos = set()
	
	p = re.compile(ur'[a-z-0-9]*\.jpe*g', re.IGNORECASE)
	for i in range(len(data)):
		test_str = data[i]
		match = re.search(p, test_str)
		photo = match.group(0)
		photos.add(photo)

	
	return len(data), len(photos)
	# with open("all_photos_data.txt", "w") as text_file:
	#     text_file.write("Number of photos: {}\n".format(len(data)))
	#     text_file.write("Number of unique photos: {}".format(len(photos)))

def write_coordinate_csv(coordinates):
	with open('coordinates.csv', 'w') as fp:
		a = csv.writer(fp, delimiter=',')
		data = coordinates
		a.writerows(data)

def write_data_csv(data):
	#latitude, longitude
	with open('data.csv', 'w') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(data)

def analyze(data):
	pass


rootdir = "/Users/Paul/Dropbox/School/Harvard/Semester 5/CS 105- Privacy and Technology/Final Project/Data"

archives = {}
geotags = []

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
		if file.endswith("coordinates_raw_data.txt"):
			archive = os.path.basename(subdir)
			path = os.path.join(subdir, file)

			data = list(import_coordinates(path))
			if len(data) > 0:
				for i in data:
					lat, lon = i
					geotags.append([archive, lat, lon])
					print archive
			coordinate_count = len(data)

			if archive in archives:
				archives[archive]["Coordinates"] = coordinate_count
			else:
				archives[archive] = dict(Coordinates=coordinate_count)

		if file.endswith("all_photos.txt"):
			archive = os.path.basename(subdir)
			path = os.path.join(subdir, file)

			complete, unique = import_all_photos(path)

			if archive in archives:
				archives[archive]["Full"] = complete
				archives[archive]["Unique"] = unique
			else:
				archives[archive] = dict(Full=complete, Unique=unique)

data = []
for key in archives:
	if "Full" in archives[key]:
		full = archives[key]["Full"]
	if "Unique" in archives[key]:
		unique = archives[key]["Unique"]
	if "Coordinates" in archives[key]:
		coordinates = archives[key]["Coordinates"]
		subdata = [key, full, unique, coordinates]
		data.append(subdata)

data.sort()
data.insert(0, ["Archive", "Full", "Unique", "Coordinates"])

geotags.sort()
geotags.insert(0, ["Archive", "Latitude", "Longitude"])

write_data_csv(data)
write_coordinate_csv(geotags)
