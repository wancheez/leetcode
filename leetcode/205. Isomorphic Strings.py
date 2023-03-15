import collections


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True
        maps = {}
        t_chars_met = set()
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char in maps and t_char not in t_chars_met:
                return False

            if s_char in maps and maps[s_char] == t_char:
                continue

            if s_char not in maps and t_char not in t_chars_met:
                maps[s_char] = t_char
                t_chars_met.add(t_char)
                continue

            return False
        return True

tests = (("paper", "title"),)
for s, t in tests:
    print(Solution().isIsomorphic(s, t))
