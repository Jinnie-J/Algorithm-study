
# O(N^2) 풀이
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        answer=0
        for i in range(len(s)):
            j=0
            d={}
            while j<=len(s)-i-1:
                if(s[i+j] not in d):
                    d[s[i+j]]=1
                    j+=1
                else:
                    answer= max(answer, j-1)
                    break
                answer= max(answer,j)

        return answer


# O(N) 풀이
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        str_list = []
        max_length = 0

        for x in s:
            if x in str_list:
                str_list = str_list[str_list.index(x)+1:]

            str_list.append(x)    
            max_length = max(max_length, len(str_list))

        return max_length