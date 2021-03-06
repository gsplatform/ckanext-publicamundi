import zope.interface
import zope.schema
import re

from ckanext.publicamundi.lib.metadata.ibase import IObject
from ckanext.publicamundi.lib.metadata.schemata import IBaseMetadata

class ICkanMetadata(IBaseMetadata):
    zope.interface.taggedValue('recurse-on-invariants', True)

