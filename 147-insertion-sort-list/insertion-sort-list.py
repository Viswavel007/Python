# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to serve as the start of the sorted list
        dummy = ListNode(0)
        curr = head
        
        while curr:
            # At each step, we save the next node to process
            next_node = curr.next
            
            # Find the correct position to insert 'curr' in the sorted list
            # We always start searching from the dummy node
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            # Insert 'curr' between 'prev' and 'prev.next'
            curr.next = prev.next
            prev.next = curr
            
            # Move to the next node in the original unsorted list
            curr = next_node
            
        return dummy.next
