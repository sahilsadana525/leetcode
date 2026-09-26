import heapq

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __lt__(self, other):
        if self.first != other.first:
            return self.first > other.first
        return self.second > other.second


class Solution:
    def reorganizeString(self, s: str) -> str:
        f = {}

        # Frequency map
        for char in s:
            f[char] = f.get(char, 0) + 1

        # Max heap
        max_heap = []

        for char, freq in f.items():
            heapq.heappush(max_heap, Pair(freq, char))

        result = ""

        while max_heap:

            current_pair = heapq.heappop(max_heap)

            # If same character as previous character
            if result and current_pair.second == result[-1]:

                # No other character available
                if not max_heap:
                    return ""

                # Take the second most frequent character
                next_pair = heapq.heappop(max_heap)

                result += next_pair.second
                next_pair.first -= 1

                if next_pair.first > 0:
                    heapq.heappush(max_heap, next_pair)

                # Put current character back
                heapq.heappush(max_heap, current_pair)

            else:
                result += current_pair.second
                current_pair.first -= 1

                if current_pair.first > 0:
                    heapq.heappush(max_heap, current_pair)

        return result