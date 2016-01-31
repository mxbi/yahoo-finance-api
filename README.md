# yahoo-finance-api
This repo contains a collection of scripts for pulling data or compiling datasets from the unofficial Yahoo Finance API, along with some documentation.

The [original API documentation](https://code.google.com/archive/p/yahoo-finance-managed/wikis/YahooFinanceAPIs.wiki) has been removed, however an unofficial one is in [**DOCUMENTATION.md**](./DOCUMENTATION.md)

## Usage

#### get_stock.py

`python get_stock.py INDEX STOCK [ARGUMENTS]`

This is a python 2 script that downloads the info about a stock, adds the current unix time, and appends it to a csv file corresponding to that stock.

The third argument is optional, and chooses what information is requested from the api. This is built by combining arguments from the [documentation](./DOCUMENTATION.md#api-arguments), eg. *vop* to download the volume, opening and closing price of a stock. If nothing is specified, the default of *sl1op* is used.

**For example:**
```python get_stock.py FTSE IHG```
will create/open a file called ```FTSE IHG.csv``` and append the following on a newline:

`"IHG",32.11,31.88,32.24,1453325715.12`

#### get_ftse.py

`python get_ftse.py [ARGUMENTS]`

This is a python 2 script that downloads information about all FTSE 100 stocks, adds the current unix time, and creates/appends to a file about each stock. This creates 100 files, and if it is run again it will append the new data to the existing 100 files.

The launch argument is optional, and and chooses what information is requested from the api. This is built by combining arguments from the [documentation](./DOCUMENTATION.md#api-arguments). If none is specified, the default of *sl1op* is used.


