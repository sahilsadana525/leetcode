class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        low,high = 0,k-1
        left = []
        right = []
        res = []
        delayed = defaultdict(int)
        left_size , right_size = 0,0
        def prune(heap,is_left):
            while heap:
                x = -heap[0] if is_left else heap[0]
                if delayed[x] == 0:
                    break
                heapq.heappop(heap)
                delayed[x]-=1
        def balance():
            nonlocal left_size, right_size
            if left_size > right_size + 1:
                p = -heapq.heappop(left)
                heapq.heappush(right,p)
                left_size-=1
                right_size+=1
                prune(left,True)
            
            elif right_size > left_size:
                p = heapq.heappop(right)
                heapq.heappush(left,-p)
                left_size+=1
                right_size-=1
                prune(right,False)

        for i in range(k):
            if not left or nums[i] <= -left[0]:
                heapq.heappush(left,-nums[i])
                left_size+=1
            else:
                heapq.heappush(right,nums[i])
                right_size+=1
            balance()
        res.append(-left[0] if k%2
        else (-left[0]+right[0])/2)

        while high < len(nums)-1:
            outgoing = nums[low]
            incoming = nums[high + 1]

            prune(left , True)
            prune(right , False)

            delayed[outgoing]+=1
            if outgoing <= -left[0]:
                left_size-=1
                if outgoing == -left[0]:
                    prune(left,True)
            else:
                right_size -= 1
                if outgoing == right[0]:
                    prune(right,False)
            
            if left and incoming <= -left[0]:
                heapq.heappush(left,-incoming)
                left_size +=1
            else:
                heapq.heappush(right,incoming)
                right_size+=1
            balance()
            prune(left,True)
            prune(right,False)
            high+=1
            low+=1
            
            if k%2:
                res.append(-left[0])
            else:
                res.append((-left[0]+right[0])/2)

        return res


