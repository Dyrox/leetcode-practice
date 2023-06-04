# Runtime: 943ms, faster than 96.72%
# Memory Usage: 30.5 MB, Beats 48.79%
# 2023-06-05 00:19

# 我寻思这不挺简单 为啥是困难问题啊

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maxdiff = 0
        if len(nums) < 2:
            return 0
        
        nums.sort()
        bruh = len(nums)
        for i in range(0,bruh-1):
            diff = nums[i+1] - nums[i]
            if diff > maxdiff:
                maxdiff = diff
        
        return maxdiff

