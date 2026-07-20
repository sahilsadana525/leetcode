class Solution:
    def find_max(self, freq):
        max_count = -1
        for i in range(256):
            max_count = max(max_count, freq[i])
        return max_count

    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = [0] * 256
        low = 0
        res = float("-inf")

        for high in range(n):
            freq[ord(s[high])] += 1

            max_cnt = self.find_max(freq)
            length = high - low + 1
            diff = length - max_cnt

            while diff > k:
                freq[ord(s[low])] -= 1
                low += 1

                max_cnt = self.find_max(freq)
                length = high - low + 1
                diff = length - max_cnt

            length = high - low + 1
            res = max(res, length)

        return res