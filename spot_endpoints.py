from binance_api import keyed_endpoint, signed_endpoint, requests

def test_order(symbol='ETHBTC', side='BUY', type='MARKET', timeInForce=None, quantity=10, quoteOrderQty=None, price=None, newClientOrderId=None, stopPrice=None, icebergQty=None, newOrderRespType=None):
	return signed_endpoint('order/test', request=requests.post, symbol=symbol, side=side, type=type, timeInForce=timeInForce, quantity=quantity, quoteOrderQty=quoteOrderQty, price=price, newClientOrderId=newClientOrderId, stopPrice=stopPrice, icebergQty=icebergQty, newOrderRespType=newOrderRespType)

def order(symbol, side, type, timeInForce=None, quantity=None, quoteOrderQty=None, price=None, newClientOrderId=None, stopPrice=None, icebergQty=None, newOrderRespType=None):
	return signed_endpoint('order', request=requests.post, symbol=symbol, side=side, type=type, timeInForce=timeInForce, quantity=quantity, quoteOrderQty=quoteOrderQty, price=price, newClientOrderId=newClientOrderId, stopPrice=stopPrice, icebergQty=icebergQty, newOrderRespType=newOrderRespType)

def cancel_order(symbol, orderId=None, origClientOrderId=None, newClientOrderId=None):
	return signed_endpoint('order', request=requests.delete, symbol=symbol, orderId=orderId, origClientOrderId=origClientOrderId, newClientOrderId=newClientOrderId)

def query_order(symbol, orderId=None, origClientOrderId=None):
	return signed_endpoint('order', symbol=symbol, orderId=orderId, origClientOrderId=origClientOrderId)

def open_orders(symbol=None):
	return signed_endpoint('openOrders', symbol=symbol)

def caoo(symbol):
	return signed_endpoint('openOrders', request=requests.delete, symbol=symbol)

def all_orders(symbol, orderId=None, startTime=None, endTime=None, limit=None):
	return signed_endpoint('allOrders', symbol=symbol, orderId=orderId, startTimer=startTime, endTime=endTime, limit=limit)

def oco(symbol, side, quantity, price, stopPrice, listClientOrderId=None, limitClientOrderId=None, limitIcebergQty=None, stopClientOrderId=None, stopLimitPrice=None, stopIcebergQty=None, stopLimitTimeInForce=None, newOrderRespType=None):
	return signed_endpoint('order/oco', request=requests.post, symbol=symbol, side=side, quantity=quantity, price=price, stopPrice=stopPrice, listClientOrderId=listClientOrderId, limitClientOrderId=limitClientOrderId, limitIcebergQty=limitIcebergQty, stopClientOrderId=stopClientOrderId, stopLimitPrice=stopLimitPrice, stopIcebergQty=stopIcebergQty, stopLimitTimeInForce=stopLimitTimeInForce, newOrderRespType=newOrderRespType)

def cancel_oco(symbol, orderListId=None, listClientOrderId=None, newClientOrderId=None):
	return signed_endpoint('orderList', request=requests.delete, symbol=symbol, orderListId=orderListId, listClientOrderId=listClientOrderId, newClientOrderId=newClientOrderId)

def query_oco(orderListId=None, origClientOrderId=None):
	return signed_endpoint('orderList', orderListId=orderListId, origClientOrderId=origClientOrderId)

def query_all_oco(fromId=None, startTime=None, endTime=None, limit=None):
	return signed_endpoint('allOrderList', fromId=fromId, startTime=startTime, endTime=endTime, limit=limit)

def account():
	return signed_endpoint('account')

def my_trades(symbol, startTime=None, endTime=None, fromId=None, limit=None):
	return signed_endpoint('myTrades', symbol=symbol, startTime=startTime, endTime=endTime, fromId=fromId, limit=limit)

def user_data_stream(request=requests.post):
	return keyed_endpoint('userDataStream', request=request)
