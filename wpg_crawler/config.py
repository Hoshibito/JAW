
"""
	Crawler Configuration
"""

import os

# maximum number of urls to be found before termination
MAX_CRAWLING_URLS_DEFAULT = 1000

# crawler time bucket before termination (in seconds)
# Default: 20 * 60  =  20 mins
TIMEOUT_BUCKET_DEFAULT = 5 * 60

# maximum crawling depth in breath-first search
MAX_CRAWLING_DEPTH_DEFAULT = 15

# maximum number of urls to be followed per depth (randomly chosen)
MAX_FOLLOWED_URLS_PER_DEPTH_DEFAULT = 25

# the amount of time to wait for each page to load (in seconds)
PAGE_LOAD_WAIT_TIME_DEFAULT = 4

# link types to filter out from crawling
FILTER_OUT_LINK_TYPES = [
'.bmp',
'.woff',
'.ttf',
'.otf'
'.css',
'.csv',
'.docx',
'.ico',
'.jpeg',
'.jpg',
'.js',
'.json',
'.pdf',
'.png',
'.svg',
'.xls',
'.xml',
'.wasm',
'.txt'
]

# name of the state script file to load a state (e.g., authentication) in the web browser
STATES_SCRIPT_FILE_NAME = "Auth"

# Enable this function to use state script files
USE_STATE_SCRIPTS = False

# the amount of time (seconds) the driver has to wait additional to any state script wait after a page load 
DRIVER_WAIT_TIME_AFTER_STATE_LOAD = 3  

# pointer to crawler directory
CRAWLER_BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# pointer to crawler parent directory
CRAWLER_PARENT_DIR = os.path.dirname(CRAWLER_BASE_DIR)

# the output filename of the crawler
URLS_SAVE_FILE_NAME = 'urls'

IS_HEADLESS_MODE = False

# whether or not save the navigation graph
SAVE_NAVIGATION_GRAPH = True

# navigation graph for sink reachability analysis
NAVIGATION_GRAPH_SAVE_FILE_NAME = "navigation_graph"


SITES_DIRECTORY = os.path.join(CRAWLER_BASE_DIR, "sites")

# directory to output the crawling data: currently in wpg-construction/outputs
OUTPUT_DATA_DIRECTORY = os.path.join(os.path.join(os.path.dirname(CRAWLER_BASE_DIR), "wpg_construction"), "outputs")


#### IMPORTANT ######
# Set your platform here
PLATFORM = "linux"


if PLATFORM == "macos":
	CHROME_DRIVER = 'chromedriver'
else:
	CHROME_DRIVER = '/usr/bin/chromedriver'

	
## whether or not the crawler should beautify JS files upon saving
## NOTE that this may incur additional time
BEAUTIFY_FILES = True


