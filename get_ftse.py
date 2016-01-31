#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import time
import sys

start_time = time.time()

def get_stock(index_name, stock_name, args):
    current_time = time.time()
    
    # Create URL
    url = "http://download.finance.yahoo.com/d/quotes.csv?s=%40%5E" + index_name + "," + stock_name + ".L&f=" + args

    # Create filename
    file_name = index_name + " " + stock_name + ".csv"
    u = urllib2.urlopen(url)
    f = open(file_name, 'ab')   # open for appending to
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    #print("Downloading to: %s" % (file_name))
    
    if len(stock_name) == 2:    # extra space added after stock name for keeping outputs equal length
        extra_space = "  "
    elif len(stock_name) == 3:
        extra_space = " "
    else:
        extra_space = ""
    # output information about stock being downloaded as single line
    print("Getting stock " + str(i + 1).ljust(3) +  ": " + ftse_list[i] + extra_space + " | filename: " + file_name + extra_space + " | Size: " + str(file_size))
    # i + 1 is used to show actual value
    # ljust makes it three characters wide           to keep in formatting
    # extra_space pads the stock name to equal width to keep in formatting

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        if "N/A" in buffer: # fails if yahoo doesnt give data
            print "N/A found in buffer. Not saved"

        else:
            # Append current time and newline to buffer
            towrite = buffer.replace('\n', '') + "," + str(current_time) + "\n"
            f.write(towrite)

        # Calculate Status of download
        #status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        #status = status + chr(8)*(len(status)+1)
        #print(status),

    f.close()
    
ftse_list = ["AAL", "ABF", "ADM", "ADN", "AHT", "ANTO", "ARM", "AV", "AZN", "BA", "BAB", "BARC", "BATS", "BDEV", "BG", "BKG", "BLND", "BLT", "BNZL", "BP", "BRBY", "BT-A", "CCH", "CCL", "CNA", "CPG", "CPI", "CRH", "DC", "DCC", "DGE", "DLG", "EXPN", "EZJ", "FRES", "GKN", "GLEN", "GSK", "HIK", "HL", "HSBA", "IAG", "IHG", "III", "IMT", "INTU", "ISAT", "ITRK", "ITV", "KGF", "LAND", "LGEN", "LLOY", "LSE", "MERL", "MKS", "MNDI", "NG", "NXT", "OML", "PFG", "PRU", "PSN", "PSON", "RB", "RBS", "RDSA", "RDSB", "REL", "RIO", "RMG", "RR", "RRS", "RSA", "SAB", "SBRY", "SDR", "SET1", "SGE", "SHP", "SKY", "SL", "SMIN", "SN", "SPD", "SSE", "STAN", "STJ", "SVT", "TPK", "TSCO", "TW", "ULVR", "UU", "VOD", "WOS", "WPG", "WPP", "WTB"] # List of FTSE constituents
i = 0   # iteration number#

if len(sys.argv) == 1:
    args = "sl1op"
else:
    args = str(sys.argv[1])

while i<99:
    #print("\nGetting stock " + str(i) + " " + ftse_list[i])
    get_stock("FTSE", ftse_list[i], args) # get stock
    i = i + 1   # move to next stock
    #time.sleep(2)
    
duration = time.time() - start_time # calculate time elapsed
print("\nCompleted all stocks! Time elapsed: " + str(duration) + " seconds")    # print final message
    