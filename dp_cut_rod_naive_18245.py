def cutRod(price, index, n):
    print("index: {} n: {}".format(index, n))
    if index == 0:
        return n*price[0]
    if (n ==0):
        return 0
    notCut = cutRod(price,index - 1,n)
    print("notCut: {} index: {} n: {}".format(notCut, index, n))
    cut = float("-inf")
    rod_length = index + 1
    #print("rod_length: {}".format(rod_length))
    if (rod_length <= n):
        print("just before cut: index: {} rod_length: {} n:{}".format(index, rod_length, n))
        cut = price[index]+cutRod(price,index,n - rod_length)
        #print("cut: {}".format(cut))
    return max(notCut, cut)

arr = [ 1, 5, 8, 9, 10, 17, 17, 20 ]
size = len(arr)
print("Maximum Obtainable Value is ",cutRod(arr, size - 1, size))
