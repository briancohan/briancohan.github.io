#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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
}

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Content Variables
DEFAULT_PROJECT_IMG = 'paul-bulai-XOQJa4OC8P0-unsplash.jpg'
NAVBAR_IMG = 'navbar.png'

EDUCATION = (
    ('University of Maryland - College Park', 'B.S. Fire Protection Engineering', 'Dec 2008'),
    ('University of Maryland - College Park', 'M.S. Fire Protection Engineering', 'Aug 2010'),
)

LICENSES = (
    ('Professional Engineer', 'VA - 0402055056', 'http://www.dpor.virginia.gov/LicenseLookup/'),
)

MEMBERSHIPS = (
    ('SFPE', 'National', 'https://www.sfpe.org/', 'PMSFPE', 2006),
    ('SFPE', 'Central Virginia', 'http://sfpecentralva.org/', 'Member at Large', 2016),
)

SOCIAL = (
    ('fab fa-linkedin-in', 'https://www.linkedin.com/in/briandcohan/'),
    ('fab fa-twitter', 'https://twitter.com/BrianDCohan'),
    ('fab fa-stack-overflow', 'https://stackoverflow.com/users/3447515/brian-cohan'),
    ('fab fa-github', 'https://github.com/briancohan'),
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
