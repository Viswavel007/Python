class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize with the first element
        max_total = nums[0]
        current_sum = 0
        
        for n in nums:
            # If current_sum becomes negative, it's better to start fresh from n
            if current_sum < 0:
                current_sum = 0
            
            current_sum += n
            
            # Update the global maximum found so far
            max_total = max(max_total, current_sum)
            
        return max_total
