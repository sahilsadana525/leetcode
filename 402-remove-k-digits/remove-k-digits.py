class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans = []
        for i in range(0,len(num)):
            while k > 0 and ans and ans[-1] > num[i]:
                ans.pop()
                k-=1
            ans.append(num[i])
        while k>0 and ans:
            ans.pop()
            k-=1
        i=0
        while i < len(ans) and ans[i]=='0':
            i+=1
        ans = ans[i:]

        return "".join(ans) if ans else "0"