class Solution:
    def findClosestElements(self,arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            distance = abs(num - x)
            # Use a max-heap behavior with heapq by negating values
            heapq.heappush(heap, (-distance, -num))
            if len(heap) > k:
                heapq.heappop(heap)
        result = [-num for _, num in heap]
        return sorted(result)
