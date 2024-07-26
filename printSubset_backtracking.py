def calcSubset(A, res, subset, index):
    res.append(subset[:])
    for i in range(index, len(A)):
        subset.append(A[i])
        calcSubset(A, res, subset, i + 1)
        subset.pop()
        

def subsets(A):
    subset = []
    res = []
    index = 0
    calcSubset(A, res, subset, index)
    return res

def AllSubsets(arr,n):
    
        def backtrack(index, path):
            # Append the current subset to the result list
            result.append(path[:])
            
            # Explore further elements to generate new subsets
            for i in range(index, n):
                # Include arr[i] in the current subset
                path.append(arr[i])
                # Move on to the next element
                backtrack(i + 1, path)
                # Backtrack by removing the last element
                path.pop()

        result = []
        backtrack(0, [])
        return result

# Driver code
if __name__ == "__main__":
    array = [1,2,3]
    # res = subsets(array)
    print(AllSubsets(array, 3))

    # # Print the generated subsets
    # for subset in res:
    #     print(*subset)