#딕셔너리 사용
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        nums.sort()
        for num in nums:
            if num in dic:
                return True
            else:
                dic[num]=1
                
        return False
      

#Set 사용
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        if len(nums) == len(numsSet):
            return False
        return True    