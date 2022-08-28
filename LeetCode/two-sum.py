# Memory Limit Code

from itertools import combinations

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        answer=[]
        
        index = [i for i in range(len(nums))]
        combi = list(combinations(nums,2))
        combi_index = list(combinations(index, 2))

        
        for i in range(len(combi)):
            if combi[i][0] + combi[i][1] == target:
                answer.append(combi_index[i][0])
                answer.append(combi_index[i][1])
                break
                
        return answer
        
        
# Accepted Code

from itertools import combinations

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic= {}
        for i,value in enumerate(nums):  #enumerate= index, value ([0,2],[1,7],[2,11],[3,15])
            find_num = target - nums[i]
            if find_num in dic:
                return [dic[find_num],i]
            
            dic[value] = i 
