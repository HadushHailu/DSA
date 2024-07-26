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


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        table = [0] * (n + 1)
        table[0] = 0
        table[1] = 1
        for i in range(2, n+1):
            table[i] = table[i-1] + table[i-2]
        return table[n]


print(fib(4))	
