def get_fib_num(value: int = 1) -> int:
	current, next = 0, 1
	step = 1
	while step < value:
		current, next = next, next + current
		step = step + 1
	return current
