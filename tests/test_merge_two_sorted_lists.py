import pytest
from leetcode.merge_two_sorted_lists import ListNode, Solution


@pytest.mark.parametrize("list1, list2, expected", [
    (ListNode(1), ListNode(2), ListNode(1, ListNode(2))),
    (
        ListNode(1, ListNode(2, ListNode(4))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))),
    ),
    (
        None, None, None
    ),
    (
        None, ListNode(0), ListNode(0),
    )

])
def test_merge_two_sorted_lists(list1, list2, expected):
    result = Solution().mergeTwoLists(list1, list2)

    while result and expected:
        assert result.val == expected.val
        result = result.next
        expected = expected.next

    assert not (result and expected)
