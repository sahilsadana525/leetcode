class Solution:
    def fun(self,a:List[int],day: int,k:int):
        c=0
        s=0
        for i in range(len(a)):
            if a[i]<=day:
                c+=1
                if c == k:
                    s+=1
                    c=0
            else:
                c = 0
        return s

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low = 1
        high = max(bloomDay)
        res=-1
        while low<=high:
            mid = (low+high)//2
            s1 = self.fun(bloomDay,mid,k)
            if m <= s1:
                res = mid
                high = mid-1
            else:
                low = mid+1
        return res




        