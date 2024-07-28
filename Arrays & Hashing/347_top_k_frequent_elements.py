from collections import defaultdict
from typing import List


# https://leetcode.com/problems/top-k-frequent-elements/description/
class Solution:
    """
    Time complexity: `O(n * k)` where `n` is the length of `nums` and `k` is `k`.
        - Technically  `O(n + k * u) where `u` is the number of unique elements in `nums`, but in the
        worst case where every number in `nums` is unique, `u` is equal to `n` so we can simplify to `O(n * k)`

    Here we count all occurrences of each element in `nums`, then iterate over our hashmap `k` times, looking for
    the `k` highest counts.

    We can optimize to `O(n)` time as shown at the end of this file by converting our hashmap such that the keys
    represent all possible frequencies, which is bounded by the length of `nums` and then returning the first `k`
    values we encounter while iterating from end to beginning. This negates the need to loop over `k`.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        topK = [None] * k
        for i in range(len(topK)):
            max_val = None
            for key, val in freq.items():
                if max_val is None or val > max_val:
                    max_val = val
                    topK[i] = key
            del freq[topK[i]]

        return topK

    def topKFrequentOptimized(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
