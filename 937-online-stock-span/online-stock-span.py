class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = 0

    def next(self, price: int) -> int:
        self.day += 1
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            p, d = self.stack.pop()
            span += d

        self.stack.append((price, span))
        return span

            




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)