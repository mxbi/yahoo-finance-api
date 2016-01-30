# yahoo-finance-api
This repo contains a collection of scripts for pulling data or compiling datasets from the unofficial Yahoo Finance API, along with some documentation.

## Usage

**get_stock.py** is a python 2 script that takes two arguments, the *stock index* and *stock name* and outputs to a csv file corresponding to the stock. If the CSV file already exists, it is appended to the end of the file.

**For example:**
```python get_stock.py FTSE IHG```
will create/open a file called ```FTSE IHG.csv``` and append the following on a newline:

`"IHG",32.11,31.88,32.24,1453325715.12`

This corresponds to ```stock ticker, current price, open price, close price, unix timestamp```


