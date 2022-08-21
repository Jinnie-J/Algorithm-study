class Solution:
    def romanToInt(self, s: str) -> int:
        d= {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        
        answer=0
        for i in range(len(s)-1):
            num = d[s[i]]
            nextNum = d[s[i+1]]
            if (num>=nextNum):
                answer+=num
            else:
                answer-=num
        answer += d[s[len(s)-1]]
        
        return answer
        