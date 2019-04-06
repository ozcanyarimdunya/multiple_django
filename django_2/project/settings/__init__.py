import logging
from .base import *

logger = logging.getLogger()

mode = os.getenv('MODE', 'DEVELOPMENT')
logger.error('Current mode: %s' % mode)

if mode == "PRODUCTION":
    from .production import *
else:
    from .local import *
