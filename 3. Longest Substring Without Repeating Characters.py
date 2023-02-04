class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexes_of_chars = {}
        max_unique_length = 0
        cur_length = 0
        cur_index = 0

        while cur_index < len(s):
            current_char = s[cur_index]
            if indexes_of_chars.get(current_char) is not None:
                last_met_ind = indexes_of_chars[current_char]
                if (cur_index - last_met_ind) <= cur_length:
                    max_unique_length = max(
                        max_unique_length,
                        cur_length,
                    )
                    cur_length = cur_index - last_met_ind

                else:
                    cur_length += 1
            else:
                cur_length += 1
            indexes_of_chars[current_char] = cur_index
            cur_index += 1
        max_unique_length = max(
            max_unique_length,
            cur_length,
        )

        return max_unique_length or len(s)

#"abcabcbb", "bbbbb", "pwwkew", 'dvdf', "abcabcabb",
tests = ("abcabcbb", "tmmzuxt",)
for test in tests:
    print(Solution().lengthOfLongestSubstring(test))
