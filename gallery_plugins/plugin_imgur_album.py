# Plugin for gallery_get.

# Each definition can be one of the following:
# - a string to match
# - a regex string to match
# - a function that takes source as a parameter and returns an array or a single match.  (You may assume that re and urllib are already imported.)
# If you comment out a parameter, it will use the default defined in __init__.py

# identifier (default = name of this plugin after "plugin_") : If there's a match, we'll attempt to download images using this plugin.
identifier = "imgur.+album.css"

# title: parses the gallery page for a title.  This will be the folder name of the output gallery.
title = r'data-title="(.*?)"'

# redirect: if the links in the gallery page go to an html instead of an image, use this to parse the gallery page.

# direct_links: if redirect is non-empty, this parses each redirect page for a single image.  Otherwise, this parses the gallery page for all images.
# * if using regex, you can have two matches: the first will be the link and the second will be the basename of the file.
#   if the matches need to be reversed, use named groups "link" and "basename"
def direct_links(source):
    start = source.find("images      :", source.find("Imgur.Album"))+14
    end = source.find("]}", start) + 2
    albumimages = []
    rawAlbumdata = source[start:end]
    if rawAlbumdata.strip():
        albumdata = eval(rawAlbumdata)
        for i in albumdata["items"]:
            albumimages.append( "http://i.imgur.com/"+i["hash"]+i["ext"] )
    return albumimages

# same_filename (default=False): if True, uses same filename from remote link.  Otherwise, creates own filename with incremental index (or uses subtitle). 