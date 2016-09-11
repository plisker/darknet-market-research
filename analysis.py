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

	print "Hey"
	# print "type:", type(data)
	# print "Count:", len(data)

def write_coordinate_csv(coordinates):
	#latitude, longitude
	with open('coordinates.csv', 'w') as fp:
		a = csv.writer(fp, delimiter=',')
		data = coordinates
		a.writerows(data)

def analyze(data):
	print "Number of unique coordinates:", len(data)


file1 = "coordinates_raw_data.txt"
file2 = "all_photos.txt"

data = import_coordinates(file1)
analyze(data)

import_all_photos(file2)

# if __name__ == "__main__":
    # # load an image through PIL's Image object
    # if len(sys.argv) < 2:
    #     print("Error! No image file specified!")
    #     print("Usage: %s <filename>" % sys.argv[0])
    #     sys.exit(1)

    # image = Image.open(sys.argv[1])
    # exif_data = get_exif_data(image)
    # latlon=get_lat_lon(exif_data)
    # if (latlon != (None, None)) and (latlon!=(0.0, 0.0)) and (latlon!=(-0.0, 0.0)) and (latlon!=(0.0, -0.0)) and (latlon!=(-0.0, -0.0)):
    #     print(sys.argv[1], latlon)
    # # print(sys.argv[1], latlon)