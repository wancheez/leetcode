# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        previous = head
        current = head.next
        last_met_duplicate = None
        first_unique = None

        while current:
            # встретили дубль
            if current.val == previous.val:
                last_met_duplicate = current
                # первый дубль?
                if not first_unique:
                    first_unique = previous
                if not current.next:
                    first_unique.next = None
            else:
                # Встретили новое
                if last_met_duplicate:  # Были дубли?
                    # убираем последовательность дублей
                    first_unique.next = current
                    first_unique, last_met_duplicate = None, None

                previous = current
            current = current.next
        return head


