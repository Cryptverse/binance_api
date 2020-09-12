import requests, urllib
from binanceAPIKey import apiKey, secretKey
from time import time, sleep
import hmac, hashlib

base_endpoint = 'https://api.binance.com'
headers = {'X-MBX-APIKEY': apiKey}
	#'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

def endpoint(endpoint, api='api', version='v3', signed=False, request=requests.get, **kwargs):
	payload={}
	if any(kwargs): 
		payload['params'] = {k:v for k,v in kwargs.items() if v is not None}
		if 'headers' in payload['params'].keys(): 
			payload['headers'] = payload['params'].pop('headers')
			if signed:
				payload['params']['timestamp'] = int(time()*1000)
				payload['params']['signature'] = hmac.HMAC(secretKey, 
								urllib.parse.urlencode(payload['params']).encode('UTF-8'),
								hashlib.sha256).hexdigest()
	r = request(f'{base_endpoint}/{api}/{version}/{endpoint}', **payload)
	if r.status_code == 429: 
		Print(r.status_code, 'sleeping')
		sleep(r.headers['Retry-After'])
	return r

def keyed_endpoint(_endpoint, api='api', version='v3', signed=False, request=requests.get, **kwargs):
	kwargs['headers']=headers
	return endpoint(_endpoint, api=api, version=version, signed=signed, request=request, **kwargs)

def signed_endpoint(endpoint, api='api', version='v3', request=requests.get, **kwargs):
	return keyed_endpoint(endpoint, api=api, version=version, signed=True, request=request, **kwargs)

