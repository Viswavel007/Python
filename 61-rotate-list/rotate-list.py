# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # 1. Calculate the length and find the actual tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # 2. Handle cases where k >= length
        k = k % length
        if k == 0:
            return head
        
        # 3. Connect tail to head to make it circular
        tail.next = head
        
        # 4. Find the new tail: it's at (length - k - 1) steps from head
        new_tail_steps = length - k
        new_tail = head
        for _ in range(new_tail_steps - 1):
            new_tail = new_tail.next
            
        # 5. Set the new head and break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
