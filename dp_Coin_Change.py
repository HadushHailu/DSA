def coinChange(C, sum, holder, res = 0, sumList=[]):
	counter = 0

	for i in C:

		#print("Previous res: {}".format(res))
		res += C[counter]
		sumList.append(C[counter])
		#print("Res: adding C[{}]: {}".format(counter, C[counter]))
		#print("current i: {} C[{}] is {} and res: {}".format(counter, counter, C[counter], res))
		#print("current list: {}".format(sumList))

		if sum - res == 0:
			print("YES FOUND: {}".format(sumList))
			#holder.add(sumList)
			#print("Holder: {}".format(holder))
			return 
 
		elif sum - res > 0:
			coinChange(C, sum, holder, res, sumList)

		else:

			res -= C[counter]
		
		sumList.pop()
		counter += 1


holder = set()
sum = 7
coins = [1,4,2]
#coinChange(coins, sum, holder)


def countWays(coins, N, sum):
	# Create a list to store the number of ways to make each value up to sum
	dp = [0] * (sum + 1)

	# There is one way to make the sum 0, which is to use no coins
	dp[0] = 1

	print("DP: {}".format(dp))

	# Iterate over each coin
	for coin in coins:
		print("[+] coin: {}".format(coin))
		# Update the dp array for values from coin to sum
		for i in range(coin, sum + 1):
			dp[i] += dp[i - coin]
			print(" [-] i: {} dp: {} dp[{}]: {}".format(i, dp, i, dp[i]))

	# The number of ways to make the sum 'sum' will be stored in dp[sum]
	return dp[sum]

# Example usage
N = 3
sum_value = 4
coins = [4,2,1]
print(countWays(coins, N, sum_value))  # Output: 4