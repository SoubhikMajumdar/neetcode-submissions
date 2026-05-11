# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        curr = head
        if not curr:
            return False
        while curr:
            if curr.next == None:
                return False
            else:
                if curr in hashset:
                    return True
                else:
                    hashset.add(curr)
            curr = curr.next 