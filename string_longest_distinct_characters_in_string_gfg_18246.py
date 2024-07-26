
def longestSubstrDistinctChars(S):
       # last index of every character
        last_idx = {}
        max_len = 0
    
        # starting index of current
        # window to calculate max_len
        start_idx = 0
    
        for i in range(0, len(S)):

            # Find the last index of str[i]
            # Update start_idx (starting index of current window)
            # as maximum of current value of start_idx and last
            # index plus 1
            if S[i] in last_idx:
                start_idx = max(start_idx, last_idx[S[i]] + 1)
    
            # Update result if we get a larger window
            max_len = max(max_len, i-start_idx + 1)
    
            # Update last index of current char.
            last_idx[S[i]] = i
            print("s[i]: {} start_idx: {} max_len: {} last_idx: {}".format(S[i], start_idx, max_len, last_idx))
    
        return max_len
s = "aewergrththy"
print(longestSubstrDistinctChars(s))
