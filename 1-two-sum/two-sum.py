class Solution(object):
    def twoSum(self, nums, target):
        for i in range (len(nums)):
            for j in range (len(nums)):
                if target==nums[i]+nums[j] and i!=j:
                    return([i,j])