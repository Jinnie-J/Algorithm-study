class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = nums[0]
        thisSum = nums[0]
        
        if len(nums)==1:
            return nums[0]
        
        for i in range(1,len(nums)):
            thisSum = max(thisSum + nums[i], nums[i])
            maxSum = max(maxSum, thisSum)
        
        return maxSum