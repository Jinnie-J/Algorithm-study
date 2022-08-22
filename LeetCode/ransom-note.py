class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        dic={}
        for word in magazine:
            if word in dic:
                dic[word]+=1
            else:
                dic[word]=1
                
        for x in ransomNote:
            if (x not in dic or dic[x]==0):
                return False
        
            dic[x]-=1
        return True