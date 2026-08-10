class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = []
        c = 0
        l.append(s[0])
        for i in range(1,len(s)):
            if len(l) != 0 and l[c] == s[i]:
                l.pop()
                c-=1
            else:
                l.append(s[i])
                c+=1
        return "".join(l)

