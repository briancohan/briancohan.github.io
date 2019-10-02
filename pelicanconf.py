#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Brian Cohan'
SITENAME = 'Brian Cohan'
SITEURL = ''
JUMBOTRON_IMAGE = 'jens-johnsson-qFYBki6u3Ik-unsplash.jpg'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = [
    'images',
    'extra',
]
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    'extra/CNAME': {'path': 'CNAME'},
    'extra/LICENSE': {'path': 'LICENSE'},
    'extra/README': {'path': 'README'},
}

LINKS = (
    ('Burnable Item Database', 'http://www.firebid.umd.edu/burning-item-database.php'),
    ('Rise Fire Database', 'http://www.sp.se/fire/fdb'),
    ('FDS', 'https://pages.nist.gov/fds-smv/'),
    ('CFAST', 'https://pages.nist.gov/cfast/'),
    ('Pathfinder', 'https://www.thunderheadeng.com/pathfinder/'),
    ('CONTAM', 'https://www.nist.gov/services-resources/software/contam'),
)

SOCIAL = (
    ('fab fa-linkedin-in', 'https://www.linkedin.com/in/briandcohan/'),
    ('fab fa-twitter', 'https://twitter.com/BrianDCohan'),
    ('fab fa-stack-overflow', 'https://stackoverflow.com/users/3447515/brian-cohan'),
    ('fab fa-github', 'https://github.com/briancohan'),
    # ('fab fa-kaggle', 'https://www.kaggle.com/briancohan'),
)

EDUCATION = (
    ('University of Maryland - College Park', 'B.S. Fire Protection Engineering', 'Dec 2008'),
    ('University of Maryland - College Park', 'M.S. Fire Protection Engineering', 'Aug 2010'),
)

LICENSES = (
    ('PE', 'VA - 0402055056'),
)

MEMBERSHIPS = (
    ('SFPE', 'National', 'PMSFPE', 2006),
    ('SFPE', 'Central VA', 'Member at Large', 2016),
)

DEFAULT_PAGINATION = 10
