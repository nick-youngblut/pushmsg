import sys
__version__ = '0.0.3'

if sys.version_info >= (3, 0):
    from pushmsg.pushmsg import *
else:
    from pushmsg import *
    
__all__ = ['pushmsg']
