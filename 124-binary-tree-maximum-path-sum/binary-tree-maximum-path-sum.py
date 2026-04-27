# Definition for a binary tree node.
class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def get_max_gain(node):
            if not node:
                return 0
            
            # 1. Recursively get the max gain from left and right subtrees
            # If a subtree returns a negative sum, we ignore it (max with 0)
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            
            # 2. Check the price of a "new path" using the current node as the peak
            current_path_sum = node.val + left_gain + right_gain
            
            # 3. Update the global maximum if the current path is better
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # 4. Return the maximum gain the parent can get from this node
            # (The parent can only pick ONE branch: left or right)
            return node.val + max(left_gain, right_gain)

        get_max_gain(root)
        return self.max_sum
