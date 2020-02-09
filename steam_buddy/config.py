import os

DATA_DIR = os.getenv('XDG_DATA_HOME', os.path.expanduser('~/.local/share'))

RESOURCE_DIR = os.getcwd()
if not os.path.isfile(os.path.join(RESOURCE_DIR, 'views/base.tpl')):
	RESOURCE_DIR = "/usr/share/steam-buddy"

SHORTCUT_DIR = DATA_DIR + '/steam-shortcuts'
BANNER_DIR = DATA_DIR + '/steam-buddy/banners'
CONTENT_DIR = DATA_DIR + '/steam-buddy/content'
