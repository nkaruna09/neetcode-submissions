class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums): # index, num 

            # check for duplicates 
            if i > 0 and n == nums[i-1]: 
                continue
            
            # 2 pointer solution 
            l, r = i+1, len(nums) - 1 
            while l < r: 
                currSum = nums[l] + nums[r]
                three_sum = n + nums[l] + nums[r]
                if three_sum > 0: 
                    r -= 1 
                elif three_sum < 0: 
                    l += 1 
                else: 
                    res.append([n, nums[l], nums[r]])
                    l += 1 
                    while nums[l] == nums[l-1] and l < r: # until no duplicates
                        l += 1 
        return res