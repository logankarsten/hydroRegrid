# Function for checking input arguments from user
# to ensure they make sense. 

import os

def checkArgs(parser):
    # Check to make sure input directory exists
    if parser.sourceDir:
        if len(parser.sourceDir[0]) == 0:
            print "ERROR: Source directory not specified."
            raise
        if not os.path.isdir(parser.sourceDir[0]):
            print "ERROR: Source directory not found."
            raise
    if parser.pattern:
        if len(parser.pattern[0]) == 0:
            print "ERROR: Input pattern not specified."
            raise
    if parser.inType:
        if len(parser.inType[0]) == 0:
            print "ERROR: inType not specified."
        if (parser.inType[0] != "GRIB") and (parser.inType[0] != "NETCDF"):
            print "ERROR: inType must be either GRIB or NETCDF"
            raise
    if parser.method:
        if (parser.method[0] < 1) or (parser.method[0] > 2):
            print "ERROR: invalid regridding method specified."
            raise
    if parser.weightPath:
        if len(parser.weightPath[0]) == 0:
            print "ERROR: weightPath not specified."
            raise
    if parser.outPath:
        if len(parser.outPath[0]) == 0:
            print "ERROR: outPath not specified."
            raise
    if not parser.shpPath:
        if not parser.geoPath:
            print "ERROR: One must specify either a polygon shapefile or geoGrid file"
            raise
    if not parser.geoPath:
        if not parser.shpPath:
            print "ERROR: One must specify either a polygon shapefil or geoGrid file"
            raise
    if parser.geoPath:
        if len(parser.geoPath) == 0:
            print "ERROR: geoPath not specified"
            raise
    if parser.shpPath:
        if len(parser.shpPath) == 0:
            print "ERROR: shpPath not specified"
            raise
