# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        currB = headB
        hashset = set()
        while currA:
            hashset.add(currA)
            currA = currA.next
        
        while currB:
            if currB in hashset:
                return currB
            currB = currB.next

        return None