class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i,num in enumerate(nums):
            complement = target-num
            if complement in seen:
                return i,seen[complement]
            else:
                seen[nums[i]] = i
        