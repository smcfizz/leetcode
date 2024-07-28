from typing import List


# https://leetcode.com/problems/encode-and-decode-strings/description/
class Solution:
    """
    Time complexity: `O(n)` for encode and `O(m)` for decode, where `n`
    is the length of `strs` and `m` is the total number of characters in the encoded string
    """
    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded.append(s[i:j])
            i = j

        return decoded

