class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        answer = 99999
        result = 0
        for i in range(len(nums)-2):
            if i>0 and nums[i-1] == nums[i]:
                continue
                
            j = i+1
            k = len(nums)-1
            
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                if abs(target-s) < answer:
                    answer = abs(target-s)
                    result = s
                
                if s == target:
                    return s
                elif s > target:
                    k-=1
                else:
                    j +=1
                    
        return result
                    
                
                    