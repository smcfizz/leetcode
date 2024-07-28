from typing import List


# https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, n in enumerate(nums):
            pair_val = target - n

            if pair_val in visited:
                return [visited[pair_val], i]

            # Don't overwrite with a later position
            if n not in visited:
                visited[n] = i
