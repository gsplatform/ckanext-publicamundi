import zope.interface
import zope.schema
import json

from ckanext.publicamundi.lib.metadata.types import *
from ckanext.publicamundi.tests import fixtures

def test_x1():
    '''Convert a valid object to/from JSON'''
    x1 = fixtures.x1

    s1d = x1.to_json(flat=False, indent=4)
    s1f = x1.to_json(flat=True, indent=4)

    x2 = InspireMetadata()
    try:
        x2.from_json(s1d, is_flat=False)
        errs2 = x2.validate()
        assert not errs2
        s2d = x2.to_json(flat=False, indent=4)
        s2f = x2.to_json(flat=True, indent=4)
        assert s1d == s2d
        assert s1f == s2f
    except Exception as ex:
        assert False, 'Cannot serialize/deserialize from (nested) JSON'

    x3 = InspireMetadata()
    try:
        x3.from_json(s1f, is_flat=True)
        errs3 = x3.validate()
        assert not errs3
        s3d = x3.to_json(flat=False, indent=4)
        s3f = x3.to_json(flat=True, indent=4)
        assert s1d == s3d
        assert s1f == s3f
    except Exception as ex:
        assert False, 'Cannot serialize/deserialize from (flattened) JSON'

if __name__ == '__main__':
    test_x1()

