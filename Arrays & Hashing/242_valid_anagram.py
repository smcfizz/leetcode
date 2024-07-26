# https://leetcode.com/problems/valid-anagram/description/
class Solution:
    # Time Complexity: O(n), or more precisely, O(s + t), where s and t are the lengths of the strings.
    # Space Complexity: Identical to the above.
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        for char in s:
            if char not in s_chars:
                s_chars[char] = 1
            else:
                s_chars[char] += 1

        t_chars = {}
        for char in t:
            if char not in t_chars:
                t_chars[char] = 1
            else:
                t_chars[char] += 1

        return s_chars == t_chars

    # I found a more "pythonic" solution after the fact.
    # It is exactly the same as the solution above, just written a bit more concise.
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        schars, tchars = {}, {}

        for i in range(len(s)):
            schars[s[i]] = 1 + schars.get(s[i], 0)
            tchars[t[i]] = 1 + tchars.get(t[i], 0)

        return schars == tchars

    # As a bonus, specifically for Python, we can do this in a single line with `return Counter(s) == Counter(t)`
