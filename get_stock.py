#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import time
import sys

current_time = time.time()      # get current time
stock_name = str(sys.argv[2])   # set stock to launch arg eg. IHG
index_name = str(sys.argv[1])   # set index to launch arg eg. FTSE

# Create URL
url = "http://download.finance.yahoo.com/d/quotes.csv?s=%40%5E" + index_name + "," + stock_name + "&f=nsl1op"

file_name = index_name + " " + stock_name + ".csv"
u = urllib2.urlopen(url)
f = open(file_name, 'ab')   # open for appending to
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    # Remove newline and stock name from buffer and inject current time
    stock = buffer.replace('\n', '').split(",",1)
    # Append current time and newline to buffer
    towrite = stock[1] + "," + str(current_time) + "\n"
    f.write(towrite) # Write to file
    
    # Status of download
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print(status),

f.close()
