class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left and not self.right:
            heapq.heappush(self.left, -num)

        else:
            if num <= -self.left[0]:
                heapq.heappush(self.left, -num)
            else:
                heapq.heappush(self.right, num)

        if len(self.left) - len(self.right) > 1:
            p = -heapq.heappop(self.left)
            heapq.heappush(self.right,p)

        if len(self.right) - len(self.left) > 1:
            p = heapq.heappop(self.right)
            heapq.heappush(self.left,-p)



        

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.left) < len(self.right):
            return self.right[0]
        else:
            return (-self.left[0]+self.right[0])/2           


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()