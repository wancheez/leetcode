# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        head1 = headA
        visited = set()
        while head1:
            visited.add(head1)
            head1 = head1.next
        head1 = headB
        while head1:
            if head1 in visited:
                return head1
            head1 = head1.next
        return None
