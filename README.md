# yahoo-finance-api
This repo contains a collection of scripts for pulling data or compiling datasets from the unofficial Yahoo Finance API, along with some documentation.

The [original API documentation](https://code.google.com/archive/p/yahoo-finance-managed/wikis/YahooFinanceAPIs.wiki) has been removed, however an unofficial one is in **DOCUMENTATION.md**

## Usage

#### get_stock.py

This is a python 2 script that downloads the info about a stock, adds the current unix time, and appends it to a csv file corresponding to that stock.

`python get_stock.py INDEX STOCK [ARGUMENTS]`

The third argument is optional, and chooses what information is requested from the api. This is built by combining arguments from the documentation, eg. *vop* to download the volume, opening and closing price of a stock. If nothing is specified, the default of *sl1op* is used.

**For example:**
```python get_stock.py FTSE IHG```
will create/open a file called ```FTSE IHG.csv``` and append the following on a newline:

`"IHG",32.11,31.88,32.24,1453325715.12`


