# This is the pre-processing module file. Several sub-routines
# are contained within here to handle pre-processing shapefiles 
# representing unstructured meshes and geoGrid files representing
# the LSM modeling domain.

from regridUtilities.logMod import logErr, logInfo, logMaster

def shpConvert(shpPath,shpUid,nodeThres,tmpDir,rank):
    from utools.prep.prep_shapefiles import convert_to_esmf_format
    from regridUtilities.argUtil import parseShpPath    
    
    try:
        parseShpPath(shpPath,unstrucPath)
    except:
        raise
        
    logMaster('Initializing pre-processing of unstructured mesh')
    convert_to_esmf_format(esmf_format, source, source_uid, \
                           node_threshold=node_threshold)