# darknet-market-research
A collection of scripts used as part of the Geotags in Dark Net Market research

*** geodata.py ***
This Python 2.7 scripts searches for geolocation data in the metadata of an image. If none if found, nothing is outputted; if geolocation data is found (and is not 0.0, 0.0), a tuple of the file's name and the latitude and longitude data will be outputted to stdout.

