import os
import random
import shutil

from tinydb import TinyDB, where

from suzune import config

_db = None


def init_db():
    if not os.path.exists(config.SUZUNE_DIR):
        os.mkdir(config.SUZUNE_DIR)
    if not os.path.exists(config.SUZUNE_DB):
        shutil.copyfile(config.SUZUNE_ORIGINAL_DB, config.SUZUNE_DB)

    global _db
    _db = TinyDB(config.SUZUNE_DB)


def get(tag):
    rows = _db.search(where('tags').test(lambda tags: tag in tags))
    if not rows:
        return ''
    return random.choice(rows)['url']


def tags():
    tags = {}
    for row in _db.all():
        for tag in row['tags']:
            if tag in tags:
                tags[tag] += 1
            else:
                tags[tag] = 1
    return sorted(tags.items())


def add(url, tags):
    _db.insert({'url': url, 'tags': tags})
