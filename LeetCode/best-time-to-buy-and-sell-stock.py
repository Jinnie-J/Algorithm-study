# Time Limit Code
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer=[]
        for i in range(len(prices)-1):
            tmp = prices[i]
            tmp_arr = prices[i+1:]
            max_value = max(tmp_arr)
            
            if max_value > tmp:
                answer.append(max_value-tmp)
                
        if len(answer)==0:
            return 0
        else:
            return max(answer)
            

# Accepted Code
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = 10000
        
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            
        return profit