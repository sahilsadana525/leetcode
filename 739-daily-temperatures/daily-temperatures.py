class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        st = []
        for i in range(0,len(temperatures)):
            while len(st)!=0 and temperatures[st[-1]]<temperatures[i]:
                index = st.pop()
                res[index] = i - index
            st.append(i)
        return res



        