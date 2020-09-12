from binance_api import endpoint

def ping():
        return endpoint('ping')

def server_time():
        return endpoint('time')

def exchange_info():
        return endpoint('exchangeInfo')

def order_book(symbol, limit=None):
        return endpoint('depth', symbol=symbol, limit=limit)

def recent_trades(symbol, limit=None):
        return endpoint('trades', symbol=symbol, limit=limit)

def old_trades(symbol, limit=None, fromId=None):
        return endpoint('historicalTrades', symbol=symbol, limit=limit, fromId=fromId, headers=headers)

def agg_trades(symbol, fromId=None, startTime=None, endTime=None, limit=None):
        return endpoint('aggTrades', symbol=symbol, fromId=fromId, startTime=startime, endTime=endTime, limit=limit)

def klines(symbol, interval, startTime=None, endTime=None, limit=None):
        return endpoint('klines', symbol=symbol, interval=interval, startTime=startTime, endTime=endTime, limit=limit)

def avg_price(symbol):
        return endpoint('avgPrice', symbol=symbol)

def ticker_24hr(symbol=None):
        return endpoint('ticker/24hr', symbol=symbol)

def ticker_price(symbol=None):
        return endpoint('ticker/price', symbol=symbol)

def book(symbol=None):
	return endpoint('ticker/bookTicker', symbol=symbol)
