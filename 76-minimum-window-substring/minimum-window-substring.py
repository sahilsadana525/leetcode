from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res = float('inf')
        len1 = 0
        start = 0
        c = defaultdict(int)
        d = defaultdict(int)
        for i in range(len(t)):
            d[t[i]]+=1
        for h in range(len(s)):
            c[s[h]]+=1
            while self.sahi(c,d):
                len1 = h - l + 1
                if res > len1:
                    res = len1
                    start = l
                c[s[l]]-=1
                l+=1
        if res==float('inf'):
            return ""
        else:
            return s[start:start+res]

    def sahi(self,c: defaultdict[str, int],d: defaultdict[str, int]):
        for i in d:
            if c[i] < d[i]:
                return False
        return True

