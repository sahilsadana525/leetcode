from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        res = 0
        c = defaultdict(int)
        for h in range(len(fruits)):
            c[fruits[h]]+=1
            while len(c)>2:
                c[fruits[l]]-=1
                if c[fruits[l]] == 0:
                    del c[fruits[l]]
                l+=1
            res = max(res,h-l+1)
        return res
