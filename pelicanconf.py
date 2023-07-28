AUTHOR = 'Samuel Colburn'
SITENAME = 'blog.sam.codes'
SITESUBTITLE = "Various projects related to code, music, games, and more"
SITEURL = 'https://blog.sam.codes'
PATH = 'blog'
THEME = 'themes/coder'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
STATIC_PATHS = ["images"]
# PHOTO_LIBRARY = "images"
# PHOTO_GALLERY = (1024, 768, 80)
# PHOTO_ARTICLE = (760, 506, 80)
# PHOTO_THUMB = (192, 144, 60)
# PHOTO_SQUARE_THUMB = False
# PHOTO_RESIZE_JOBS = 5

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Old Blog', 'https://hoob.dev'),
)

# Social widget
SOCIAL = (
    ('@sam.codes', 'https://bsky.app/profile/sam.codes'),
)

DEFAULT_PAGINATION = 15
RELATIVE_URLS = True
MENUITEMS = [
    ("About", 'hello-world.html')
]
