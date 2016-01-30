# Unofficial documentation

## How to call the API

All requests begin with a base url of `http://finance.yahoo.com/d/quotes.csv` and have arguments added onto the end.

The name of the requested stock is added through `?s=%40%5E`index`,`stock. eg. `?s=%40%5EDJI,GOOG` for Google stock.

##### Data to download

You then need to choose the data to request. This is done by appending a `&f=` followed by the different arguments. *The list of arguments is available at the bottom of this file.*

There are a huge number of data pieces you can download. Many of these were ambigous in the original documentation, and I haven't figured out exactly what they refer to e.g. the difference between **ask** and **ask (realtime)**, so I've left them how they appear in the original docs.

These can be concatenated eg. if you wanted to download the ask, bid and change in percent you would use `&f=abp2`

##### Ratelimit

According to the [Yahoo general API documentation](https://developer.yahoo.com/yql/guide/usage_info_limits.html), usage is capped at 2,000 requests/hour. This doesn't seem to apply to the finance API however, as I've performed 8,000 requests in 15 minutes before returning HTTP error 999. No true figure is known.

##### Examples

`http://download.finance.yahoo.com/d/quotes.csv?s=%40%5EFTSE,ARM.L&f=sl1vop`

This will return the stock ticker, current price, volume, opening price and closing price for the stock `FTSE` `ARM.L`

## API Arguments

| Argument | Meaning |
| --- | --- |
| a | Ask |
| y | Dividend Yield |
| b | Bid |
| d | Dividend per Share |
| b2 | Ask (Realtime) |
| r1 | Dividend Pay Date |
| b3 | Bid (Realtime) |
| q | Ex-Dividend Date |
| p | Previous Close |
| o | Open |
| c1 | Change |
| d1 | Last Trade Date |
| c | Change &amp; Percent Change |
| d2 | Trade Date |
| c6 | Change (Realtime) |
| t1 | Last Trade Time |
| k2 | Change Percent (Realtime) |
| p2 | Change in Percent |
| c8 | After Hours Change (Realtime) |
| m5 | Change From 200 Day Moving Average |
| c3 | Commission |
| m6 | Percent Change From 200 Day Moving Average |
| g | Day's Low |
| m7 | Change From 50 Day Moving Average |
| h | Day's High |
| m8 | Percent Change From 50 Day Moving Average |
| k1 | Last Trade (Realtime) With Time |
| m3 | 50 Day Moving Average |
| l | Last Trade (With Time) |
| m4 | 200 Day Moving Average |
| l1 | Last Trade (Price Only) |
| t8 | 1 yr Target Price |
| w1 | Day's Value Change |
| g1 | Holdings Gain Percent |
| w4 | Day's Value Change (Realtime) |
| g3 | Annualized Gain |
| p1 | Price Paid |
| g4 | Holdings Gain |
| m | Day's Range |
| g5 | Holdings Gain Percent (Realtime) |
| m2 | Day's Range (Realtime) |
| g6 | Holdings Gain (Realtime) |
| k | 52 Week High |
| v | More Info |
| j | 52 week Low |
| j1 | Market Capitalization |
| j5 | Change From 52 Week Low |
| j3 | Market Cap (Realtime) |
| k4 | Change From 52 week High |
| f6 | Float Shares |
| j6 | Percent Change From 52 week Low |
| n | Name |
| k5 | Percent Change From 52 week High |
| n4 | Notes |
| w | 52 week Range |
| s | Symbol |
| s1 | Shares Owned |
| x | Stock Exchange |
| j2 | Shares Outstanding |
| v | Volume |
| a5 | Ask Size |
| b6 | Bid Size |
| k3 | Last Trade Size |
| t7 | Ticker Trend |
| a2 | Average Daily Volume |
| t6 | Trade Links |
| i5 | Order Book (Realtime) |
| l2 | High Limit |
| e | Earnings per Share |
| l3 | Low Limit |
| e7 | EPS Estimate Current Year |
| v1 | Holdings Value |
| e8 | EPS Estimate Next Year |
| v7 | Holdings Value (Realtime) |
| e9 | EPS Estimate Next Quarter |
| s6 | Revenue |
| b4 | Book Value |
| j4 | EBITDA |
| p5 | Price / Sales |
| p6 | Price / Book |
| r | P/E Ratio |
| r2 | P/E Ratio (Realtime) |
| r5 | PEG Ratio |
| r6 | Price / EPS Estimate Current Year |
| r7 | Price / EPS Estimate Next Year |
| s7 | Short Ratio |
