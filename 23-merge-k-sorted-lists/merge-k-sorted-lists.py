import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min-heap to store (value, list_index, node_object)
        min_heap = []
        
        # Initial step: Put the head of each list into the heap
        for i, l in enumerate(lists):
            if l:
                # We include index 'i' to handle cases where multiple nodes have the same value
                heapq.heappush(min_heap, (l.val, i, l))
        
        dummy = ListNode(0)
        curr = dummy
        
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            
            # Attach the smallest node to our result list
            curr.next = node
            curr = curr.next
            
            # If the extracted node has a next node, push it into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        return dummy.next
