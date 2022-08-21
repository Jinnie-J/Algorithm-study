# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        arr=deque()
        
        if head is None:
            return True
        
        while head:
            arr.append(head.val)
            head=head.next
            
        while len(arr)>1:
            if arr.popleft() != arr.pop():
                return False
        return True
                