import csv
import numpy as np
import re

def import_coordinates(file):
	with open(file) as f:
		data = f.readlines()

	coordinates = set()

	for i in range(len(data)):
		data[i] = eval(data[i])
		x, y = data[i]
		coordinates.add(y)

	write_coordinate_csv(list(coordinates))
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

	with open("all_photos_data.txt", "w") as text_file:
	    text_file.write("Number of photos: {}\n".format(len(data)))
	    text_file.write("Number of unique photos: {}".format(len(photos)))

def write_coordinate_csv(coordinates):
	#latitude, longitude
	with open('coordinates.csv', 'w') as fp:
		a = csv.writer(fp, delimiter=',')
		data = coordinates
		a.writerows(data)

def analyze(data):
	with open("coordinates_data.txt", "w") as text_file:
	    text_file.write("Number of unique coordinates: {}".format(len(data)))

try:
	file1 = "coordinates_raw_data.txt"
	file2 = "all_photos.txt"

	data = import_coordinates(file1)
	analyze(data)

	import_all_photos(file2)
except:
	pass

