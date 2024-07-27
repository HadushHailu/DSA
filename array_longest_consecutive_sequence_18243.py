def longestConsecutive(nums: list[int]) -> int:
    lenConsSeq = 0
    startIdx = 0
    nums.sort()

    for i in range(1,len(nums)):
        if nums[i] == (nums[i-1]) or nums[i] == (nums[i-1] + 1):
            continue
        else nums[i] != (nums[i-1] + 1):
            thisCutLen = len(nums[startIdx:i])
            if thisCutLen > lenConsSeq:
                lenConsSeq = thisCutLen
            startIdx = i
    
    thisCutLen = len(nums[startIdx:])
    if thisCutLen > lenConsSeq:
        lenConsSeq = thisCutLen

    return lenConsSeq
        
l = [0,2,1,1]
print(longestConsecutive(l))
