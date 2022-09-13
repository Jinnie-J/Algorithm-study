# Time Limit Code
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            arr1=[]
            arr2=[]
            if i!=0:
                arr1 = nums[:i]
                
            if i!=len(nums)-1:
                arr2 = nums[i+1:]                
            
            arr_sum = reduce(lambda x, y: x * y, arr1+arr2)
            answer.append(arr_sum)
            
        return answer


# Accepted Code
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        temp=1
        for i in range(len(nums)):
            answer.append(temp)
            temp *= nums[i]
            
        temp=1
        for i in range(len(nums)-1,-1,-1):
            answer[i]*=temp
            temp *= nums[i]
            
        return answer      