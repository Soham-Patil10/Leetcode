class Solution(object):
    def countCommas(self, n):
        if n < 1000:
            return 0
        ans = 0
        power = 1000

        while power <= n:
            ans += n - power + 1
            power *= 1000

        return ans
        