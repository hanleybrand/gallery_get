# Plugin for gallery_get.
import re,urllib

# Each definition can be one of the following:
# - a string
# - a regex string
# - a function that takes source as a parameter and returns an array or a string.  (You may assume that re and urllib are already imported.)
# If you comment out a parameter, it will use the default defined in __init__.py

# identifier (default = name of this plugin after "plugin_") : If there's a match, we'll attempt to download images using this plugin.

# title: parses the gallery page for a title.  This will be the folder name of the output gallery.
title = r'<title>(.+?)</title>'

# redirect: if the links in the gallery page go to an html instead of an image, use this to parse the gallery page.

# direct_links: if redirect is non-empty, this parses each redirect page for a single image.  Otherwise, this parses the gallery page for all images.
def direct_links(source):
    links = re.findall('href=[\"\'](/photo/.+)[\"\']',source)
    subpage = urllib.urlopen("http://www.imagefap.com" + links[0]).read()
    return re.findall('(http://x.fap.to/images/full/.+?\.jpg)',subpage)

# same_filename (default=False): if True, uses filename specified on remote link.  Otherwise, creates own filename with incremental index. 