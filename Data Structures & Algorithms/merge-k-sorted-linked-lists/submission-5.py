# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []

        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))
        
        # print(heap)

        dummy = ListNode()
        curr = dummy
        
        while(heap):

            node = heapq.heappop(heap)
            curr.next = node[2]

            if node[2].next:
                heapq.heappush(heap,(node[2].next.val,node[1],node[2].next))
            
            curr = curr.next
        
        # curr = dummy.next
        # while(curr):
        #     print(curr.val)
        #     curr = curr.next
        
        return dummy.next
            

            

            

            



        