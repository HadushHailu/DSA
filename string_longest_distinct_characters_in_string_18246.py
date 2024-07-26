def longestSubstring(S)->int:
    holder = []
    cut = []

    for i in range(len(S)):
        print(S[i])
        if S[i] in cut:
            print("Cut: {}".format(cut))
            holder.append(cut)
            cut = []
        cut.append(S[i])
    # Append the last cut
    holder.append(cut)

    print(holder)

    longest = holder[0]
    for x in holder:
        if len(x) > len(longest):
            longest = x
    return len(longest)
        

s="aewergrththy"
longest = longestSubstring(s)
print("return: {0}".format(longest))
