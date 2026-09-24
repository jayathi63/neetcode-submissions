# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        curr = head

        slow = curr
        fast = curr
        pre_mid = None
        while(fast and fast.next):
            pre_mid = slow
            slow = slow.next
            fast = fast.next.next
            

        mid = slow

        curr = mid

        pre = None

        while(curr):
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        
        if pre_mid:
            pre_mid.next = pre


        
        curr1 = head
        curr2 = pre
        
        curr = head
        while(curr1 != pre and curr2):
            next1 = curr1.next
            next2 = curr2.next


            curr.next = curr1
            curr = curr.next
            curr.next = curr2
            curr = curr.next

            curr1 = next1
            curr2 = next2

            
        

            



        