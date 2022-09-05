class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrom(left,right):
            #펠린드롬 조건에 맞는 동안 while문 진행. 조건에 맞지 않는 순간이 오면 전 단계의 left, right index 반환
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        
        #s의 길이가 1 이거나, s 자체가 펠린드롬 일 경우 먼저 확인
        if len(s)<2 or s == s[::-1]:
            return s
        
        answer=""
        for i in range(len(s)-1):
            #짝수 길이의 펠린드롬 일 경우, 연속하는 두 글자에서 앞 뒤로 한글자씩 늘려가며 확인
            #홀수 길이의 펠린드롬 일 경우, 한 칸을 뛴 두 글자에서 앞 뒤로 한 글자씩 늘려가며 확인
            answer = max(answer, palindrom(i,i+1), palindrom(i,i+2), key = len)
            
        return answer
            
        