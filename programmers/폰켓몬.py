def solution(nums):
    answer = 0
    num = len(nums) // 2
    set_nums = set(nums);
    if len(set_nums) >= num:
        answer = num
    else:
        answer = len(set_nums)
    return answer

# 간단한 풀이

def solution(nums):
    return min(len(nums)/2, len(set(nums)))