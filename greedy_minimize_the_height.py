def getMinDiff(arr, n, k):
    # Sort the array
    arr.sort()

    # Initialize the difference between the maximum and minimum heights
    ans = arr[n - 1] - arr[0]

    # The smallest possible height and the largest possible height after modification
    smallest = arr[0] + k
    largest = arr[n - 1] - k

    # Iterate through the array
    for i in range(n - 1):
        min_height = min(smallest, arr[i + 1] - k)
        max_height = max(largest, arr[i] + k)

        # Skip negative heights
        if min_height < 0:
            continue

        # Update the answer with the minimum difference found
        ans = min(ans, max_height - min_height)

    return ans

# Example usage
k = 2
arr = [1, 5, 8, 10]
n = len(arr)
print("Minimum difference is", getMinDiff(arr, n, k))  # Output: 5
