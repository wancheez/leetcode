class Solution:
    def strStr1(self, haystack: str, needle: str) -> int:
        found_lens = []  # len and start_position
        for cur_ind, char in enumerate(haystack):
            updated_list = found_lens[:]
            for variant in found_lens:
                if char == needle[variant[0]]:
                    variant[0] += 1
                    if variant[0] == len(needle):
                        return cur_ind + 1 - variant[0]
                else:
                    updated_list.remove(variant)
            found_lens = updated_list
            if char == needle[0]:
                if needle == char:
                    return cur_ind
                found_lens.append([1, cur_ind])
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1

    def strStr3(self, haystack: str, needle: str) -> int:
            if needle == "":
                return 0
            for i in range(len(haystack) + 1 - len(needle)):
                if haystack[i: i+len(needle)] == needle:
                    return i
            return -1

    def prefix_func(self, input: str):
        result = [0, ]
        for i in range(1, len(input)):
            result.append(0)
            j = result[i - 1]
            while j >= 0:
                if input[i] == input[j]:
                    result[i] = j + 1
                    break
                j -= 1
        return result

    def kmp(self, string: str):
        if string == "":
            return []
        lps = [0]*len(string)

        prevLPS, i = 0, 1
        while i < len(string):
            if string[i] == string[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i+=1
            elif prevLPS <= 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]
        return lps

    def strStr_kmp(self, haystack: str, needle: str) -> int:
        result = [0, ]
        input = f'{needle}#{haystack}'
        for i in range(1, len(input)):
            result.append(0)
            j = result[i - 1]
            while j >= 0:
                if input[i] == input[j]:
                    result[i] = j + 1
                    if result[i] == len(needle):
                        return i - 2*len(needle)
                    break
                j -= 1
        return -1

    def strStr_kmp2(self, haystack: str, needle: str) -> int:
        string = f'{needle}#{haystack}'

        lps = [0] * len(string)

        prevLPS, i = 0, 1
        while i < len(string):
            if string[i] == string[prevLPS]:
                lps[i] = prevLPS + 1
                if lps[i] == len(needle):
                    return i - 2*len(needle)
                prevLPS += 1
                i += 1
            elif prevLPS <= 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]
        return -1



tests = (("mississippi", "issipi"), ("sadbutsad", "sad"), ("oa", "a"), ("mississippi", "issip"), ("leetcode", "leeto"), ("asadbutsad", "sad"),)
print(Solution().prefix_func("abacaba"))
print(Solution().prefix_func("abababa"))
print(Solution().prefix_func("aabaaab"))
print(Solution().prefix_func("issipi#mississippi"))


print(Solution().kmp("abacaba"))
print(Solution().kmp("abababa"))
print(Solution().kmp("aabaaab"))
print(Solution().kmp("issipi#mississippi"))

for haystack, needle in tests:
    print(Solution().strStr_kmp2(haystack, needle))
