import os
from urllib import request as req

def downloader(from_url, to_file): 
    if not os.path.isfile(to_file):
        req.urlretrieve(from_url, to_file)