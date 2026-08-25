# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split and reverse the second half
        second = slow.next
        slow.next = None

        prev = None
        while second:
            nextnode = second.next
            second.next = prev
            prev = second
            second = nextnode

        # 3. Merge the two halves
        first, second = head, prev

        while second:
            node1 = first.next
            node2 = second.next

            first.next = second
            second.next = node1

            first = node1
            second = node2
