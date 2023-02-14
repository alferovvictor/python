def fib(value):
	def f(prev2, prev1, step, max):
		if step == max:
			return prev2 + prev1
		
		if step == 1:
			return f(0, 1, step + 1, max)
		
		if step == 2:
			return f(0, 1, step + 1, max)
		
		return f(prev1, prev2 + prev1, step + 1, max)	
	
	return f(0, 0, 1, value)

print(fib(100))