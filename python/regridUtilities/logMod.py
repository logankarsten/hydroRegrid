# Utility functions to handle logging from calling program.

from mpi4py import MPI
import logging

MPI_COMM = MPI.COMM_WORLD
MPI_RANK = MPI_COMM.Get_rank()

def initLog(pId,cDate,logDir):
    import logging
    # Create log file path
    logPath = logDir + "/REGRID_JOB_RANK" + str(MPI_RANK) + str(pId) + \
              "_" + cDate + ".LOG"
    print logPath
    logging.basicConfig(filename=logPath,level=logging.DEBUG)
        
    logging.info('Program initialized from rank: ' + str(MPI_RANK))

def logErr(msg):
    logging.error(msg + ": " + str(MPI_RANK))
    
def logInfo(msg):
    logging.info(msg + ": " + str(MPI_RANK))
    
def logMaster(msg):
    if MPI_RANK == 0:
        logging.info(msg + ": from master")