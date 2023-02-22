import collections
from fibonacci_fastapi_test import FibonacciFastApiTest

base_url = 'http://127.0.0.1:8000/'

Test = collections.namedtuple('Test', ['cls', 'instance'])

tests: list[Test] = []
tests.append(Test(cls=FibonacciFastApiTest, instance=FibonacciFastApiTest(base_url)))

for test in tests:
	for method_name in dir(test.cls):
		if method_name.startswith('__'):
			continue
		
		print(f'calling method: {method_name}')
		method = getattr(test.cls, method_name)
		method(test.instance)

print('PASSED')