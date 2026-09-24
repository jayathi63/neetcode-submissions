# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeTwoLists(head1, head2):
            curr1 = head1
            curr2 = head2

            head = ListNode()
            curr = head

            while(curr1 and curr2):
                if curr1.val < curr2.val:
                    curr.next = curr1
                    curr1 = curr1.next
                else:
                    curr.next = curr2
                    curr2 = curr2.next
                curr = curr.next
            
            if curr1:
                curr.next = curr1
            if curr2:
                curr.next = curr2
            
            return head.next
        
        while(len(lists) > 1):
            merged = []

            for i in range(0,len(lists),2):
                # print(i,i+1)
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(mergeTwoLists(l1,l2))
            
            lists = merged




        return lists[0] if lists else None
            

            



        