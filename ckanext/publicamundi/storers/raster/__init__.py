import sys

__all__ = [ 
    'supported_formats',
    'gdal',
    'ogr',
    'osr',
]

supported_formats = [
    'geotiff',
    'png',
    'jpeg',
]

wcs_output_formats = {
    'rasdaman': [
        { 'display_name': 'CSV', 'name': 'csv' },
        { 'display_name': 'JPEG', 'name': 'jpeg' },
        { 'display_name': 'JPEG 2000', 'name': 'jpeg2000' },
        { 'display_name': 'NetCDF', 'name': 'netcdf' },
        { 'display_name': 'PNG', 'name': 'png' },
        { 'display_name': 'TIFF', 'name': 'tiff' },
    ],
}

temp_dir = None

gdal = None

ogr = None

osr = None

def setup(gdal_folder, temp_folder):
    '''The module needs to be explicitly setup (before being used) when certain 
    config parameters are available.

    Note that this module is imported from both `publicamundi_raster` plugin and 
    from our Celery tasks (which acquire their configuration in very different ways).
    '''
    
    # Setup temporary folders

    global temp_dir

    temp_dir = temp_folder 

    # Update sys paths in order to link to GDAL library and import osgeo
    # Fixme: This is a workaround, normally we should not update sys paths!
            
    if not gdal_folder in sys.path:
        sys.path.append(gdal_folder)

    # Import and configure osgeo library

    from osgeo import gdal as _gdal, ogr as _ogr, osr as _osr
    
    global gdal, ogr, osr
    
    gdal, ogr, osr = _gdal, _ogr, _osr
   
    osr.UseExceptions()
    ogr.UseExceptions()

    return
