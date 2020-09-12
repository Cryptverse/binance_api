from websockets import connect

class Websocket(connect):

	def __init__(self, stream_name):
		base_endpoint = 'wss://stream.binance.com:9443'
		super().__init__(f'{base_endpoint}/ws/{stream_name}')

#	async def subscribe(self, stream_name):
#		await self.send({'method':'SUBSCRIBE', 'params':[stream_name], 'id':id})
#		response =  await self.recv()
#		if response['result'] is None:
#			id += 1
#		return response					


