class Solution(object):
    def maxPalindromes(self, s, k):
        n = len(s)
        best_start = [-1] * n
        def scan(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k: 
                    best_start[r] = max(best_start[r], l)
                    return
                l -= 1
                r += 1
        for i in range(n):
            scan(i, i)          
            scan(i, i + 1)         
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]           
            l = best_start[i - 1]
            if l >= 0:
                dp[i] = max(dp[i], dp[l] + 1)        
        return dp[n]