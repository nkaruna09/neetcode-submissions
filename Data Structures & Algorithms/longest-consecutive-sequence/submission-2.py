class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in numSet: # going through each number in the list
            if (n-1) not in numSet: # if there is no number less than this, we start building up the sequence
                length = 1 # reset the sequence to one
                while (n + length) in numSet: 
                    length += 1 #increase the length each time you find the next sequence
                longest = max(length, longest)

        return longest # returns the longest consecutive sequence
        