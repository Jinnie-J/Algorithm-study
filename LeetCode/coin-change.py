#Dynamic Programming 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [-1] * (amount+1)
        dp[0]=0
        
        for i in range(amount+1):
            value = 987654321
            
            if dp[i]!= -1:
                continue
            # dp[i] = 현재 index - 각 동전을 하나 뺐을 때의 index의 배열 값 + 1     
            for coin in coins:
                x = i - coin
                if (x<0 or dp[x]==-1):
                    continue
                    
                value = min(dp[x]+1, value)
                
            if value == 987654321:
                dp[i] = -1
            else:
                dp[i] = value
                
        return dp[amount]