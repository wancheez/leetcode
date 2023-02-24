import pytest
from leetcode.palindrome_number import Solution


@pytest.mark.parametrize("num, expected", [
    (1000021, False),
    (121, True),
    (-11221, False),
    (10, False),
    (0, True),
])
def test_merge_two_sorted_lists(num, expected):
    result = Solution().isPalindrome(num)
    assert result == expected
