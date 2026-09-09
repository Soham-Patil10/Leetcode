class Solution(object):
    def countCommas(self, n):
        total = 0
        p = 1000
        while p <= n:
            total += n - p + 1
            p *= 1000
        return total
        