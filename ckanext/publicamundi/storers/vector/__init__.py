import sys

__all__ = [
    'supported_formats',
    'gdal',
    'ogr',
    'osr',
]

supported_formats = [
    'shapefile',
    'kml',
    'gml',
    'gpx',
    'geojson',
    'sqlite',
    'geopackage',
    'gpkg'
]

wfs_output_formats = {
    'geoserver': [
        { 'display_name': 'CSV', 'name': 'csv' },
        { 'display_name': 'GML2', 'name': 'GML2' },
        { 'display_name': 'GML3.1', 'name': 'text/xml; subtype=gml/3.1.1' },
        { 'display_name': 'GML3.2', 'name': 'application/gml+xml; version=3.2' },
        { 'display_name': 'GeoJSON', 'name': 'application/json' },
        { 'display_name': 'KML', 'name': 'application/vnd.google-earth.kml+xml' },
        { 'display_name': 'Shapefile', 'name': 'SHAPE-ZIP' }
    ],
}

temp_dir = None

gdal = None

ogr = None

osr = None

def setup(gdal_folder, temp_folder):
    '''The module needs to be explicitly setup (before being used) when certain 
    config parameters are available.

    Note that this module is imported from both `publicamundi_vector` plugin and 
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
