def fib(n, cache={}):
	if n in cache:
		result = cache[n]
		print("Getting fib({}) as {}".format(n, cache[n]))

	elif n == 0:
		result = 0
	elif n == 1:
		result =  1
	else:
		result = fib(n-1) + fib(n-2)

	cache[n] = result
	print("Calculating fib({})".format(n))
	return result


print(fib(4))	
