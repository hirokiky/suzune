import os

import suzune

SUZUNE_DIR = os.path.expanduser('~/.suzune/')
SUZUNE_DB = os.path.join(SUZUNE_DIR, 'db.json')
SUZUNE_ORIGINAL_DB = os.path.join(os.path.abspath(list(suzune.__path__)[0]), './data/db.json')
