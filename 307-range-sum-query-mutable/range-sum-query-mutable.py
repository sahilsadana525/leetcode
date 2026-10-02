class NumArray:

    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0]*(4*self.n)
        self.build(0,0,self.n-1)
    
    def build(self,i,start,end):
        if start == end:
            self.tree[i] = self.nums[start]
            return
        mid = (start+end)//2
        self.build(2*i+1,start,mid)
        self.build(2*i+2,mid+1,end)
        self.tree[i] = self.tree[2*i+1] + self.tree[2*i+2]
    
    def update_segment(self,i,start,end,index,val):
        if start == end:
            self.tree[i] = val
            self.nums[index] = val
            return 
        mid = (start+end)//2
        if index <= mid:
            self.update_segment(2*i+1,start,mid,index,val)
        else:
            self.update_segment(2*i+2,mid+1,end,index,val)
        self.tree[i] = self.tree[2*i+1] + self.tree[2*i+2]

    def range_sum(self,i,start,end,l,r):
        if l>end or r<start:
            return 0 
        if l<=start and end<=r:
            return self.tree[i]
        mid = (start+end)//2
        left = self.range_sum(2*i+1,start,mid,l,r)
        right = self.range_sum(2*i+2,mid+1,end,l,r)
        return left + right


    def update(self, index: int, val: int) -> None:
        self.update_segment(0,0,self.n-1,index,val)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.range_sum(0,0,self.n-1,left,right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)