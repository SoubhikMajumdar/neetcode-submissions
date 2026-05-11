# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        l2 = list2
        l1=list1
        while l2 and l1:
            if l1.val < l2.val:
                tail.next = l1
                l1=l1.next
            else:
                tail.next = l2
                l2=l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next