import sys

__version__ = '0.0.1'

if sys.version_info >= (3, 0):
    from pushnote.pushnote import *
else:
    from pushnote import *

__all__ = ['pushnote']
