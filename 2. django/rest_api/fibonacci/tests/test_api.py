import requests
import json

tests = [(1, 0), (2, 1), (3,1), (4,2), (5,3)]

class FibonacciApiTest():
	def __init__(self, base_url: str):
		self.base_url = base_url
	
	def fib_get_test(self):    
		for test in tests:
			order = test[0]
			expected = test[1]
			url = self.base_url + 'api/fib/?order=' + str(order)
			x = requests.get(url)
			value = int(x.content) 
			assert value == expected, f"value: {value}, expected: {expected}"

	def fib_post_test(self):    
		for test in tests:
			order = test[0]
			expected = test[1]

			data = {"order": order}
			url = self.base_url + 'api/fib/'
			x = requests.post(url, json=data)
			data = json.loads(x.content)
			value = int(data["value"]) 
			assert value == expected, f"value: {value}, expected: {expected}"
