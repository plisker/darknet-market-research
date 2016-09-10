# from https://gist.github.com/moshekaplan/5330395
# which was derived from https://gist.github.com/erans/983821


## Use Python2.7, NOT Python3
import sys
import csv

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif_data(image):
    """Returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags"""
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for gps_tag in value:
                    sub_decoded = GPSTAGS.get(gps_tag, gps_tag)
                    gps_data[sub_decoded] = value[gps_tag]

                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value

    return exif_data
    
def _convert_to_degress(value):
    """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
    deg_num, deg_denom = value[0]
    d = float(deg_num) / float(deg_denom)

    min_num, min_denom = value[1]
    m = float(min_num) / float(min_denom)

    sec_num, sec_denom = value[2]
    s = float(sec_num) / float(sec_denom)
    
    return d + (m / 60.0) + (s / 3600.0)

def get_lat_lon(exif_data):
    """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
    lat = None
    lon = None

    if "GPSInfo" in exif_data:      
        gps_info = exif_data["GPSInfo"]

        gps_latitude = gps_info.get("GPSLatitude")
        gps_latitude_ref = gps_info.get('GPSLatitudeRef')
        gps_longitude = gps_info.get('GPSLongitude')
        gps_longitude_ref = gps_info.get('GPSLongitudeRef')

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _convert_to_degress(gps_latitude)
            if gps_latitude_ref != "N":                     
                lat *= -1

            lon = _convert_to_degress(gps_longitude)
            if gps_longitude_ref != "E":
                lon *= -1

    return lat, lon


################
# Example ######
################
if __name__ == "__main__":
    # load an image through PIL's Image object
    if len(sys.argv) < 2:
        print("Error! No image file specified!")
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)

    image = Image.open(sys.argv[1])
    exif_data = get_exif_data(image)
    latlon=get_lat_lon(exif_data)
    if (latlon != (None, None)) and (latlon!=(0.0, 0.0)) and (latlon!=(-0.0, 0.0)) and (latlon!=(0.0, -0.0)) and (latlon!=(-0.0, -0.0)):
        print(sys.argv[1], latlon)
    # print(sys.argv[1], latlon)