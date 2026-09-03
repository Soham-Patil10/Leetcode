class Solution(object):
    def uniformArray(self, nums1):
         n = len(nums1)
         if n == 1:
            return True
         arr = sorted(nums1)
         target_parity = arr[0] % 2
         has_smaller_odd = (arr[0] % 2 == 1)
         for k in range(1, n):
             x = arr[k]
             px = x % 2
             if px != target_parity:
                 if not has_smaller_odd:
                     return False

             if px == 1:
                 has_smaller_odd = True
         return True