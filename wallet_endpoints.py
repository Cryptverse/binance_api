from binance_api import endpoint, signed_endpoint, requests

def system_status():
	return endpoint('systemStatus.html', 'wapi')

def my_coins():
	return signed_endpoint('capital/config/getall', 'sapi', 'v1')
	
def account_snapshot(type='SPOT', startTime=None, endTime=None, limit=None):
	return signed_endpoint('accountSnapshot', 'sapi', 'v1', type=type, startTime=startTime, endTime=endTime, limit=limit)

def disable_fast_withdraw_switch():
	return signed_endpoint('account/disableFastWithdrawSwitch', 'sapi', 'v1', requests.post)

def enable_fast_withdraw_switch():
	return signed_endpoint('account/enableFastWithdrawSwitch', 'sapi', 'v1', requests.post)

def withdraw(coin, address, amount, network=None, addressTag=None, name=None):
	return signed_endpoint('capital/withdraw/apply', 'sapi', 'v1', requests.post, coin=coin, address=address, amount=amount,
				network=network, addressTag=addressTag, name=name)

def deposit_history_sn(coin=None, status=None, startTime=None, endTime=None, offset=None):
	return signed_endpoint('capital/deposit/hisrec', 'sapi', 'v1', coin=coin, status=status, startTime=startTime,
				endTime=endTime, offset=offset)

def deposit_history(asset=None, status=None, startTime=None, endTime=None):
	return signed_endpoint('depositHistory.html', 'wapi', asset=asset, status=status, startTime=startTime,
				endTime=endTime)

def withdraw_history_sn(coin=None, status=None, offset=None, limit=None, startTime=None, endTime=None):
	return signed_endpoint('capital/withdraw/history', 'sapi', 'v1', coin=coin, tatus=status, offset=offset, startTime=startTime,
				endTime=endTime)
def withdraw_history(asset=None, status=None, startTime=None, endTime=None):
	return signed_endpoint('withdrawHistory.html', 'wapi', asset=asset, status=status, startTime=startTime,
				endTime=endTime)

def address_sn(coin, network=None):
	return signed_endpoint('capital/deposit/address', 'sapi', 'v1', coin=coin, network=network)

def address(asset, status=None):
	return signed_endpoint('depositAddress.html', 'wapi', asset=asset, status=status)

def account_status():
	return signed_endpoint('accountStatus.html', 'wapi')

def api_status():
	return signed_endpoint('apiTradingStatus.html', 'wapi')

def dust_log():
	return signed_endpoint('userAssetDribbletLog.html', 'wapi')

def transfer_dust(*asset):
	return signed_endpoint('asset/dust', 'sapi', 'v1', asset=asset)

def dividends(asset=None, startTime=None, endTime=None, limit=None):
	return signed_endpoint('asset/assetDividend', 'sapi', 'v1', asset=asset, startTime=startTime, endTime=endTime, limit=limit)

def asset_detail():
	return signed_endpoint('assetDetail.html', 'wapi')

def trade_fee(symbol=None):
	return signed_endpoint('tradeFee.html', 'wapi', symbol=symbol)

