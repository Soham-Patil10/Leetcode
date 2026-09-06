class Solution(object):
    def numDistinct(self, s, t):
        n, m = len(s), len(t)
        if m > n:
            return 0
        dp = [0] * (m + 1)
        dp[0] = 1 
        for i in range(1, n + 1):
            char_s = s[i - 1]
            for j in range(m, 0, -1):
                if char_s == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[m]
        