class Solution(object):
    def minElement(self, nums):
        min_count = float('inf')
        for num in nums:
            count = 0
            digit = 0
            while num>0:
                digit = num%10
                count += digit
                num = num//10
            if count<min_count:
                min_count = count
        return min_count