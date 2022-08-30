# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        s1=""
        while(l1):
            s1+=str(l1.val)
            l1=l1.next
            
        s1= s1[::-1]
        
        s2=""
        while(l2):
            s2+=str(l2.val)
            l2=l2.next
        
        s2= s2[::-1]

        sum_val = str(int(s1)+ int(s2))
        
        answer= ListNode(sum_val[len(sum_val)-1])
        head=answer
        
        for i in range(len(sum_val)-2 , -1, -1):
            answer.next = ListNode(sum_val[i])
            answer= answer.next
        
        return head
         
        
        