# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        len = 0
        curr = head

        while curr:
            len+=1
            curr = curr.next
        
        print(len)

        curr = head
        k = len-n+1
        i = 1
        pre = None

        while(curr and i < k):
            pre = curr
            curr = curr.next
            i+=1
        
        # print(curr.val, pre.val)

        if pre and curr:
            pre.next = curr.next
        elif curr == head:
            head = curr.next
        else:
            pre.next = None


        return head
        