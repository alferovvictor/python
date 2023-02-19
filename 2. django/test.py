import requests
import json

base_url = 'http://127.0.0.1:8000/'

tests = [(1, 0), (2, 1), (3,1), (4,2), (5,3)]

def fib_get_test():    
	for test in tests:
		order = test[0]
		expected = test[1]
		url = base_url + 'api/fib/?order=' + str(order)
		x = requests.get(url)
		value = int(x.content) 
		assert value == expected, f"value: {value}, expected: {expected}"

def fib_post_test():    
	for test in tests:
		order = test[0]
		expected = test[1]

		data = {"order": order}
		url = base_url + 'api/fib/'
		x = requests.post(url, json=data)
		data = json.loads(x.content)
		value = int(data["value"]) 
		assert value == expected, f"value: {value}, expected: {expected}"

fib_get_test()
fib_post_test()
print('PASSED')