# Main running program for regridding using ESMF.

# Logan Karsten
# National Center for Atmospheric Research
# Research Applications Laboratory

import sys, os
from mpi4py import MPI

# Set path to include internal library
cwd = os.getcwd()
pathTmp = cwd + "/python"
sys.path.insert(0,pathTmp)

import sys, os
import argparse
from regridUtilities.argUtil import checkArgs
from regridUtilities.logMod import initLog, logErr, logMaster, logInfo
from regridUtilities.preProcMod import shpConvert
import datetime

MPI_COMM = MPI.COMM_WORLD
MPI_RANK = MPI_COMM.Get_rank()

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
    parser.add_argument('--shpUid', nargs='?', help='Unique Identifier for Shapefile.')
    parser.add_argument('--nodeThresh', nargs='?', help='Number of nodes to cutoff.')
    
    args = parser.parse_args()
    
    # Ensure arguments provided by user are sane
    if MPI_RANK == 0:
        try:
            checkArgs(args)
        except:
            print "ERROR: Improper arguments passed."
            sys.exit(1)

    # Set default node threshold. For any unstructured polygons with a number
    # of vertices above this number, they will be broken up to reduce 
    # large ragged arrays.
    if not parser.nodeThresh:
        nodeThresh = 10000
        
    # Initiate log file to store log messages on
    pId = os.getpid()
    cDate = datetime.datetime.now()
    cDate = cDate.strftime('%Y_%m_%d_%H_%M_%S')
    logDir = cwd + "/log"
    initLog(pId,cDate,logDir)

    # Establish temporary directory, which will hold temporary
    # files during pre-processing, weight generation, and regridding
    tmpDir = cwd + "/tmp"
    
    # First check to see if weight file already exists. If it does,
    # forego pre-processing and go straight to pre-processing source 
    # data for regridding. 
    if os.path.isfile(parser.weightPath):
        try:
            shpConvert(shpPath,shpUid,nodeThresh,tmpDir,MPI_RANK)
        except:
            logErr('Pre-Processing of shapefile failed. Program exiting.')
            sys.exit(1)
    else:
        if parser.shpPath:
            
            # Call routine to pre-process shp file
        elif parser.geoPath:
            # Call routine to pre-process geoGrid file
        
    
if __name__ == "__main__":
    main(sys.argv[1:])