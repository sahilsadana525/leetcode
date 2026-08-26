class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, h = 0, n - 1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[n - 1]:
                # mid is in the left sorted part
                if nums[mid] < target:
                    l = mid + 1
                else:
                    if target >= nums[0]:
                        h = mid - 1
                    else:
                        l = mid + 1

            else:
                # mid is in the right sorted part
                if nums[mid] > target:
                    h = mid - 1
                else:
                    if nums[n - 1] >= target:
                        l = mid + 1
                    else:
                        h = mid - 1

        return -1



        