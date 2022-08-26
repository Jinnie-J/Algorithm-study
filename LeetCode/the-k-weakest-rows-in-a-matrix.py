class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []
        for i in range(len(mat)):
            arr.append((i, sum(mat[i])))
        sorted_arr = sorted(arr, key=lambda x: x[1])
        
        answer = [idx[0] for idx in sorted_arr[:k]]
        
        return answer
