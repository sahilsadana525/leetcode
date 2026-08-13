class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i,j = 0,0
        last = 0
        last1 = 0
        n = len(nums1) + len(nums2)
        if n % 2 != 0:
            for t in range(n//2+1):
                if i < len(nums1):
                    if j < len(nums2) and nums1[i] > nums2[j]:
                        last = nums2[j]
                        j+=1
                    else:
                        last = nums1[i]
                        i+=1
                else:
                    last = nums2[j]
                    j+=1
            return last
        else:
            for t in range(n//2):
                if i < len(nums1):
                    if j < len(nums2) and nums1[i] > nums2[j]:
                        last = nums2[j]
                        j+=1
                    else:
                        last = nums1[i]
                        i+=1
                else:
                    last = nums2[j]
                    j+=1

            if i < len(nums1):
                if j < len(nums2) and nums1[i] > nums2[j]:
                    last1 = nums2[j]
                    j+=1
                else:
                    last1 = nums1[i]
                    i+=1
            else:
                last1 = nums2[j]
                j+=1
        return (last + last1) / 2