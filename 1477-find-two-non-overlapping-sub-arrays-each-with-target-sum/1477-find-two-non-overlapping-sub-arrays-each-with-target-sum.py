class Solution(object):
    def minSumOfLengths(self, arr, target):
        INF = float('inf')
        n = len(arr)
        best = [INF] * n   
        ans = INF
        l = 0
        window = 0
        for r in range(n):
            window += arr[r]
            while window > target:
                window -= arr[l]
                l += 1
            cur = INF
            if window == target:
                cur = r - l + 1
                if l > 0 and best[l - 1] < INF:
                    ans = min(ans, cur + best[l - 1])
            best[r] = min(best[r - 1] if r > 0 else INF, cur)
        return -1 if ans == INF else ans
        