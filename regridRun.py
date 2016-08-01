# Main running program for regridding using ESMF.

# Logan Karsten
# National Center for Atmospheric Research
# Research Applications Laboratory

import sys, os

# Set path to include internal library
cwd = os.getcwd()
pathTmp = cwd + "/python"
sys.path.insert(0,pathTmp)

import sys, os
import argparse
from regridUtilities.argUtil import checkArgs
from regridUtilities.argUtil import logging
#from regridUtilities.preProc import shpConvert
import datetime

def main(argv):
    # Parse arguments passed in.
    parser = argparse.ArgumentParser(description='Main program to regrid ' + \
                                     'to either a modeling domain, or an ' + \
                                     'an unstructured mesh grid.')
    parser.add_argument('sourceDir', type=str, nargs='+',
                        help='Source directory containing data to be processed')
    parser.add_argument('pattern', type=str, nargs='+', 
                        help='Pattern of files to look for, I.E. - name.t12z')
    parser.add_argument('inType', type=str, nargs='+',
                        help='Input type, either GRIB or NETCDF')
    parser.add_argument('method', type=int, nargs='+',
                        help='Regrid method (1-2)')
                        # 1 = bilinear
                        # 2 = conservative 1st order
    parser.add_argument('weightPath', type=str, nargs='+',
                        help='Weight file path')
                        # Specify path, even if file does not exist. 
                        # It will be created if not found.
    parser.add_argument('outPath', type=str, nargs='+',
                        help='Output NetCDF path')
                        # Specify output path to store NetCDF file.
    parser.add_argument('--shpPath', nargs='?', help='Input polygon shapefile')
    parser.add_argument('--geoPath', nargs='?', help='Input LSM geoGrid file.')
    
    args = parser.parse_args()
    
    # Ensure arguments provided by user are sane
    try:
        checkArgs(args)
    except:
        print "ERROR: Improper arguments passed."
        sys.exit(1)
        
    # Initiate log file to store log messages on
    pId = os.getpid()
    cDate = datetime.datetime.now()
    cDate = cDate.strftime('%Y_%m_%d_%H_%M_%S')
    logDir = cwd + "/log"
    logging(pId,cDate,logDir)        
    
if __name__ == "__main__":
    main(sys.argv[1:])