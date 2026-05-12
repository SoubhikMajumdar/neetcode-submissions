# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        count=0
        
        while curr.next:
            count+=1
            curr=curr.next

        # element to be removed is: (count - n +1)th element
        removeNode = count-n+1
        i =0
        curr = dummy
        
        while curr.next:
            i+=1
            if i == removeNode:
                curr.next = curr.next.next
                break
            curr = curr.next

        return dummy.next
