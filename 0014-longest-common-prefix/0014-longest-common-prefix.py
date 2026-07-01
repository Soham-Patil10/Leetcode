class Solution(object):
    def longestCommonPrefix(self, strs):
        ref = strs[0]
        for i in range(len(ref)):
          for s in strs:
            if i >= len(s) or s[i] != ref[i]:
                return ref[:i]
        return ref
        