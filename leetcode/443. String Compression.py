import math


class Solution:
    def compress1(self, chars: list[str]) -> int:
        char_count = 1
        pointer = 1
        char_num = 1
        while char_num < len(chars):
            if chars[char_num] != chars[char_num - 1]:
                if char_count == 1:
                    pointer += 1
                elif char_count < 10:
                    chars[pointer] = str(char_count)
                    pointer += 2
                else:
                    num_list = self._int_to_tuple(char_count)
                    chars[pointer:0] = num_list
                    pointer += len(num_list)
                chars[pointer] = chars[char_num]

                char_count = 1
            else:
                char_count += 1
            char_num += 1
        if char_count > 1:
            num_list = self._int_to_tuple(char_count)
            chars[pointer:0] = num_list
            pointer += len(num_list)
        return pointer

    def compress(self, chars: list[str]) -> int:
        insert_pointer = 1
        current_count = 1
        pointer = 1
        chars.append(None)
        while pointer < len(chars):
            if chars[pointer] != chars[pointer - 1]:
                if current_count == 1:
                    pass
                elif current_count < 9:
                    chars[insert_pointer] = str(current_count)
                    insert_pointer += 1
                else:
                    num_list = str(current_count)
                    chars[insert_pointer:insert_pointer + len(num_list)] = num_list
                    insert_pointer += len(num_list)
                chars[insert_pointer] = chars[pointer]
                insert_pointer += 1
                current_count = 1
            else:
                current_count += 1
            pointer += 1
        return insert_pointer - 1


tests = (["a", "a", "a", "b", "b", "a", "a"],
["a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b",
 "b", "b", "b", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
["a", "a", "a", "b", "b", "a", "a"], ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
["a", "a", "b", "b", "c", "c", "c"], ["a"])
for test in tests:
    print(Solution().compress(test))
