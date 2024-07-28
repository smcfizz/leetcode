from collections import Counter, defaultdict
from typing import List


# https://leetcode.com/problems/group-anagrams/description/
class Solution:
    """
    The approach below operates in `O(n * m * l)` time, where `n` is the size of `strs`,
    `m` is the average length of each word in `strs`, and `l` is the number of groups of the same length

    One optimization that could be made is to use a list representing the count of each character in a word
    as the key to the `anagrams` dict instead of the number of letters in each word. This would remove the
    need to store multiple lists under the same key and consequently the requirement of flattening the dict
    before returning the result. Such an optimization would result in a time complexity of `O(n * m)`.
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            if len(word) not in anagrams:
                anagrams[len(word)] = [[word]]
                continue

            groups = anagrams[len(word)]
            found = False
            for i, group in enumerate(groups):
                if Counter(group[0]) == Counter(word):
                    anagrams[len(word)][i].append(word)
                    found = True
                    break

            if not found:
                anagrams[len(word)].append([word])

        return [item for sublist in anagrams.values() for item in sublist]

    def groupAnagramsOptimized(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()