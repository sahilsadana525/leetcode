# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        st = []
        a = []
        res = []
        while head!=None:
            a.append(head.val)
            head = head.next
        n = len(a)
        res = [0]*n
        res[n-1] = 0
        st.append(a[n-1])
        for i in range(n-2,-1,-1):
            while len(st)!=0 and st[-1]<=a[i]:
                st.pop()
            if len(st)==0:
                res[i] = 0
            else:
                res[i] = st[-1]
            st.append(a[i])
        return res