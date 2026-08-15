class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binsearch(nums,target,True)
        right = self.binsearch(nums,target,False)
        return [left,right]
    def binsearch(self,nums,target,leftBais):
        l,h = 0,len(nums) - 1
        i=-1
        while l<=h:
            mid = (l+h)//2
            if nums[mid]<target:
                l = mid+1
            elif nums[mid]>target:
                h = mid-1
            else:
                i = mid
                if leftBais:
                    h = mid-1
                else:
                    l = mid+1
        return i
