# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        source_head = head
        list_len = 1
        while head.next:
            head = head.next
            list_len += 1

        cur_ind = 1
        head = source_head
        if n == list_len:
            return head.next
        while cur_ind < list_len - n:
            head = head.next
            cur_ind += 1
        if head.next:
            head.next = head.next.next
        else:
            head.next = None
        return source_head


#test = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
#test = ListNode(1, ListNode(2))
test = ListNode(1, None)
Solution().removeNthFromEnd(test, 1)