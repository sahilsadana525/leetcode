class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        st.append([s[0],1])
        c = ""
        for i in range(1,len(s)):
            if len(st)!=0 and st[-1][0] == s[i]:
                st[-1][1]+=1
                if st[-1][1] == k:
                    st.pop()
            else:
                st.append([s[i],1])
        for ch, count in st:
            c += ch * count
        return c
