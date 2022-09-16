class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)        
        dp = [False]* (n+1)
        dp[0]=True
        
        # s의 한글자 씩 확인하며, wordick에 포함되어 있는지 확인
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]