from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        if not slow or not slow.next or not slow.next.next:
            return False
        slow = slow.next
        fast = fast.next.next
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

print(Solution().hasCycle(first))
pass