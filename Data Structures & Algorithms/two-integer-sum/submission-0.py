class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {} # val -> index
        for i, num in enumerate(nums):  
            difference = target - num
            if difference in diff_map: 
                return [diff_map[difference], i]
            diff_map[num] = i 

        