from .base import *
in_production = eval(os.getenv('PRODUCTION'))

if in_production:
    from .prod import *
else:
    from .dev import *
