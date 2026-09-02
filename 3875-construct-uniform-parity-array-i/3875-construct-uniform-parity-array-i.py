class Solution(object):
    def uniformArray(self, nums1):
        n = len(nums1)
        odd_count = sum(1 for x in nums1 if x % 2 == 1)
        can_all_odd = odd_count >= 1
        can_all_even = odd_count == 0 or odd_count >= 2
        return can_all_odd or can_all_even
        