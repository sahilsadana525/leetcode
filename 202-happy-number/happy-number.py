class Solution:
    def square(self,n:int):
        sum1 = 0
        while n > 0:
            d = n%10
            n = n//10
            sum1 = sum1 + d*d
        return sum1
    def isHappy(self, n: int) -> bool:
        slow,fast = n,n
        while fast != 1:
            slow = self.square(slow)
            fast = self.square(fast)
            fast = self.square(fast)
            if slow == fast and slow!=1:
                return False
        return True
        