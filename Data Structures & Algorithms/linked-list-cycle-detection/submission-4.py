# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        curr = head
        if not curr: # if it doesnt exist then obvs false
            return False
        while curr:
            if curr.next == None: #if we reach None, then it's not cyclic and ave reached end of LL
                return False
            else:
                if curr in hashset: #if the listnode object already in hashset then we know it's cyclic
                    return True
                else:
                    hashset.add(curr) # if havent seen in hash we can now add it to hashset
            curr = curr.next 