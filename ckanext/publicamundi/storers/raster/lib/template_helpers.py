import urllib
from pylons import config

import ckanext.publicamundi.storers.raster as rasterstorer

def get_wcs_output_formats(backend='rasdaman'):
    return rasterstorer.wcs_output_formats.get(backend, {})

def get_wcs_coverage_url(service_endpoint, coverage_name, output_format):
    '''Build a WCS ProcessCoverages request url
    '''
    
    # Note A more proper place for this would be a WCSRequest class, similar to
    # the existing WCSTRequest class.

    qs_params = (
        ('service', 'WCS'), 
        ('version', '2.0.1'), 
        ('request', 'ProcessCoverages'),
        ('query', 'for c in (%s) return encode(c, "%s")' % (
            coverage_name, output_format)),
    )

    qs = '&'.join((k + '=' + urllib.quote(v) for k, v in qs_params))
    return service_endpoint + '?' + qs
