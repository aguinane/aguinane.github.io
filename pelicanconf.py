#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Default Settings
AUTHOR = 'Alex Guinane'
COPYRIGHT_NAME = AUTHOR
SITENAME = 'Alex Guinane'
SITETITLE = SITENAME
SITESUBTITLE = 'The blog formerly known as [Tales From Turgi]'
SITE_SUMMARY = 'Personal blog of Alex Guinane'
SITELOGO = '/images/avatar.jpg'
FAVICON = '/favicon.ico'
TIMEZONE = 'Australia/Brisbane'
DEFAULT_DATE_FORMAT = ('%d %b %Y')
DEFAULT_LANG = 'en'

# Output paths
PATH = 'content'
ARTICLE_EXCLUDES = ['extra']

STATIC_PATHS = ['images',
                'extra/CNAME',
                'extra/favicon.ico',
                'extra/robots.txt',
                'extra/google5e801b1078ff9818.html',
                ]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/google5e801b1078ff9818.html': {'path': 'google5e801b1078ff9818.html'},
}

# Theme Settings
THEME = 'themes/custom'
RESPONSIVE_IMAGES = True

# Plugin settings
PLUGIN_PATHS = ['pelican-plugins', 'plugins']
PLUGINS = ['representative_image',
           'advthumbnailer',
           'clean_summary',
           'sitemap',
           'similar_posts',
           ]
IMAGE_PATH = 'images'           
ADVTHUMB_SEARCH_IMAGES_IN_ANCHORS = False
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    },
    'exclude': []
}

# Blogroll
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_LINKS_ON_MENU = True
MENUITEMS = (
    ('Archives', '/archives.html'),
)
LINKS = (
    ('Blog', '/blog_index.html'),
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)

INDEX_SAVE_AS = 'blog_index.html'
ARTICLE_URL = 'posts/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Social widget
GITHUB_URL = "https://github.com/aguinane"
TWITTER_USERNAME = "alexguinane"
SOCIAL = (
    ("twitter", 'https://twitter.com/alexguinane'),
    ("github", 'https://github.com/aguinane'),
    ("linkedin", 'https://www.linkedin.com/in/alexguinane/'),
    ("rss", '/feeds/all.rss.xml'),
)


# Feed generation is usually not desired when developing
SUMMARY_MAX_LENGTH = 25
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = 12
