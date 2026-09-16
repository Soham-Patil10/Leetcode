class Solution(object):
    def numberOfSets(self, n, k):       
        m, r = n + k - 1, 2 * k
        c = 1
        for i in range(r):
            c = c * (m - i) // (i + 1)
        return c % (10**9 + 7)    