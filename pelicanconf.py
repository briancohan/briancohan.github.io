#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from functools import partial

# Site Info
AUTHOR = 'Brian Cohan'
SITENAME = 'Brian Cohan'
SITEURL = ''
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en-us'

# Site Generation
PATH = 'content'
THEME = 'themes/cohan'
DEFAULT_PAGINATION = 12
DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = [
    'images',
    'extra',
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}
PLUGIN_PATHS = ['plugins/pelican-plugins']
PLUGINS = ['autopages']

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Content Variables
DEFAULT_PROJECT_IMG = 'paul-bulai-XOQJa4OC8P0-unsplash.jpg'
NAVBAR_IMG = 'navbar.png'

SOCIAL = (
    ('fab fa-linkedin-in', 'https://www.linkedin.com/in/briandcohan/'),
    ('fab fa-twitter', 'https://twitter.com/BrianDCohan'),
    ('fab fa-stack-overflow', 'https://stackoverflow.com/users/3447515/brian-cohan'),
    ('fab fa-github', 'https://github.com/briancohan'),
    ('fab fa-strava', 'https://www.strava.com/athletes/38661281')
    # ('fab fa-kaggle', 'https://www.kaggle.com/briancohan'),
)

LINKS = (
    ('Burnable Item Database', 'http://www.firebid.umd.edu/burning-item-database.php'),
    ('Rise Fire Database', 'http://www.sp.se/fire/fdb'),
    ('FDS', 'https://pages.nist.gov/fds-smv/'),
    ('CFAST', 'https://pages.nist.gov/cfast/'),
    ('Pathfinder', 'https://www.thunderheadeng.com/pathfinder/'),
    ('CONTAM', 'https://www.nist.gov/services-resources/software/contam'),
)

JINJA_FILTERS = {
    'sort_by_article_count': partial(
        sorted,
        key=lambda tags: len(tags[1]),
        reverse=True)}
