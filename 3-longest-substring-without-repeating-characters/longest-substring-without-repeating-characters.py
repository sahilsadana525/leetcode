from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        c = defaultdict(int)
        res = 0
        for h in range(len(s)):
            c[s[h]]+=1
            k = h - l + 1
            while len(c) < k:
                c[s[l]]-=1
                if c[s[l]] == 0:
                    del c[s[l]]
                l+=1
                k = h - l + 1
            len1 = h - l + 1
            res = max(res,len1)
        return res