# 2차원 배열 풀이
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []
        for i in range(len(mat)):
            arr.append((i, sum(mat[i])))
        sorted_arr = sorted(arr, key=lambda x: x[1])
        
        answer = [idx[0] for idx in sorted_arr[:k]]
        
        return answer

# 딕셔너리 풀이
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic = {}
        for i in range(len(mat)):
            dic[i]= sum(mat[i])
        sorted_dic = sorted(dic.items(), key=lambda x: x[1])
        
        answer=[]
        for i in range(k):
            answer.append(sorted_dic[i][0])
        return answer
