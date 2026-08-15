class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,h = 0,len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while l<=h:
            mid = (l+h)//2
            if mid == len(nums)-1 and nums[mid] != nums[mid-1]:
                return nums[mid]
            if mid == 0 and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if nums[mid]!= nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            elif mid> 0 and nums[mid] == nums[mid-1]:
                if (h - mid) % 2 == 0:
                    h=mid-2
                else:
                    l = mid+1
            elif mid < len(nums)-1 and nums[mid] == nums[mid+1]:
                if (h - mid+1) % 2 == 0:
                    h=mid-1
                else:
                    l = mid+2
                