from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        result_head = result
        while l1 or l2:
            if not l1:
                current_l1 = 0
            else:
                current_l1 = l1.val

            if not l2:
                current_l2 = 0
            else:
                current_l2 = l2.val

            sum_vals = current_l1 + current_l2
            if sum_vals > 9:
                result.val = sum_vals % 10
                if l1.next:
                    l1.next.val += sum_vals // 10
                else:
                    l1.next.val = ListNode(sum_vals // 10)
            else:
                result.val = sum_vals

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            result.next = ListNode(0)
            previous = result
            result = result.next
        if result.val == 0:
            previous.next = None
        return result_head


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
res = Solution().addTwoNumbers(l1, l2)
pass