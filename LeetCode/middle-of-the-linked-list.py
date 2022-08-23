# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length=0
        tmp=head
        while tmp:
            length+=1
            tmp=tmp.next
            
        length //= 2
        
        while length>0:
            head = head.next
            length-=1
            
        return head