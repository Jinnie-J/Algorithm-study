#dp 사용 풀이
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        arr = [1] * len(nums)
        
        for i in range(1,len(nums)):
            max_value=1
            for j in range(i):
                if nums[i]>nums[j]:
                    max_value = max(max_value, arr[j]+1)
                    
            arr[i]=max_value
            
        return max(arr)

#binary search 사용 풀이
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [] 
        arr.append(nums[0])
        
        for num in nums[1:]:
            if arr[-1] < num: 
                arr.append(num)
            else:
                sorted_idx = bisect.bisect_left(arr, num) 
                arr[sorted_idx] = num
        
        return len(arr)