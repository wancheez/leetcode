from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for str in strs:
            group = res[tuple(sorted(str))]
            group.append(str)
        return list(res.values())


tests = (["",""], [""], ["eat", "tea", "tan", "ate", "nat", "bat"],)
for test in tests:
    print(Solution().groupAnagrams(test))
