class Solution:
    def fun(self, s: str, order: List[int], k: int, time: int):
        n = len(s)

        # positions that have become *
        marked = [False] * n

        for i in range(time + 1):
            marked[order[i]] = True

        total = n * (n + 1) // 2

        # Count substrings containing no *
        no_star = 0
        length = 0

        for i in range(n):
            if not marked[i]:
                length += 1
            else:
                no_star += length * (length + 1) // 2
                length = 0

        # last segment
        no_star += length * (length + 1) // 2

        return total - no_star

    def minTime(self, s: str, order: List[int], k: int) -> int:
        low = 0
        high = len(order) - 1
        res = -1
        while low <= high:
            mid = (low + high)//2
            s1 = self.fun(s,order,k,mid)
            if s1 >= k:
                res = mid
                high = mid-1
            else:
                low = mid+1
        return res
        