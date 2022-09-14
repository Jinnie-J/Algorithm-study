class Solution:
    def maxProduct(self, nums: List[int]) -> int:        
        prev_min = nums[0]
        prev_max = nums[0]
        answer = nums[0]
        
        if len(nums)==1:
            return nums[0]
        
        # 양수*양수 / 음수*음수 / 양수*음수 확인
        for i in range(1,len(nums)):
            tmp = prev_max
            
            prev_max = max(nums[i], prev_min * nums[i], prev_max * nums[i])
            prev_min = min(nums[i], prev_min * nums[i], tmp * nums[i])
            answer = max(answer, prev_max)
        
        return answer