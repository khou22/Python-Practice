import requests
import urllib

# Progress bar
import time
import sys

# Access other directories
import os

logo = requests.get('http://static.wixstatic.com/media/b0f00e_d7d035fd659a497eae7fb745a3d81171.png_srz_84_84_85_22_0.50_1.20_0.00_png_srz')
logo.raise_for_status() # Callback if page not found

# Response 200 is a success, 404 is a failure
logo.status_code == requests.codes.ok

# Simple console progress indicator
# for i in range(100):
    # time.sleep(1)
    # sys.stdout.write("\r%d%%" % i)
    # sys.stdout.flush()

def reporthook(blocknum, blocksize, totalsize): # built in callback for urlretrieve
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        sys.stdout.write("\r%d%%" % percent)
        sys.stdout.flush() # No line break
    else: # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))

url = "http://www.mfiles.co.uk/mp3-downloads/purcell-funeral-music-for-queen-mary.mp3"
fileName = "test.mp3"
path = os.path.expanduser("~/Desktop/" + fileName)
urllib.urlretrieve(url, path, reporthook)
print("") # Line break

print("Finished")
