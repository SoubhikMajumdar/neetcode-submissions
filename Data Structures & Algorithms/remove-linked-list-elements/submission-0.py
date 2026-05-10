# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            if curr.val != val:
                arr.append(curr.val)
            curr = curr.next
        if not arr:
            return None
        res = ListNode(arr[0])
        curr = res
        for i in range(1,len(arr)):
            node = ListNode(arr[i])
            curr.next = node
            curr = curr.next
        return res
        