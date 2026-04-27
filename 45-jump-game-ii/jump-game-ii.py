class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        
        # We don't need to jump if we are already at the last element
        # So we iterate up to len(nums) - 1
        for i in range(len(nums) - 1):
            # Update the farthest point reachable from current position
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of the range for the current jump
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Optimization: if we can already reach the end, break early
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps
