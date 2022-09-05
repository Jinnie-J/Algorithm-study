class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        answer=0
        
        #투포인터 방식 (특정한 합을 가지는 부분 연속 수열을 찾는 문제에 사용)
        #길이가 최대인 두 점(0, len(height)-1) 부터 시작하여, 포인터를 좁혀나가면서 최대값 구하기
        while left < right:
            answer = max(answer, ((right - left) * min(height[left], height[right])))
            
            if height[left] < height[right] :
                left+=1
            else:
                right-=1
            
        return answer