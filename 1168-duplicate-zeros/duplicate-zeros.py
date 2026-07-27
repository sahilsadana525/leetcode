from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        possible_dups = 0
        last = n - 1

        # Count the zeros that can actually be duplicated
        for left in range(last + 1):
            if left > last - possible_dups:
                break

            if arr[left] == 0:
                # Edge case: zero at the boundary
                if left == last - possible_dups:
                    arr[last] = 0
                    last -= 1
                    break
                possible_dups += 1

        # Start copying from the end
        last_index = last - possible_dups

        for i in range(last_index, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]