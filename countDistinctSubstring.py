def countDistinctSubstring(s):
    substrings = set()

    # Generate all possible substrings
    for i in range(len(s)):
        current_substring = ""
        print("current i: {}".format(i))
        for j in range(i, len(s)):
            current_substring += s[j]
            print(current_substring)
            substrings.add(current_substring)
    
    # Add 1 for the empty substring
    return len(substrings) + 1

# Example usage
s = "ababa"
print(countDistinctSubstring(s))  # Output: 10
