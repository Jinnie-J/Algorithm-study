# 런타임 오류 발생 코드
import heapq

def solution(program):
    answer = []
    waiting_list=[]
    time = 0
    program.sort(key = lambda x:x[1])
    waiting_list=[]
    while program or not len(waiting_list)==0:
        while len(program) > 0 and program[0][1] <= time:
            heapq.heappush(waiting_list, program.pop(0))

        now_program = heapq.heappop(waiting_list)
        answer.append([now_program[0], time-now_program[1]])
        time += now_program[2]
    
    result=[0] * 11
    result[0]= time
    for i in range(1, len(answer)):
        result[answer[i][0]] += answer[i][1]
    
    
    return result


# 개선한 코드
def solution(program):
    answer = [0] * 11
    
    program.sort(key = lambda x:x[1])
    heap=[]
    time= 0
    
    while len(program) > 0 or not len(heap) == 0:
        if len(heap)==0:
            time = program[0][1]
            while len(program) >0 and program[0][1] <= time:
                heapq.heappush(heap, program.pop(0))
        tmp = heapq.heappop(heap)
        answer[tmp[0]] += (time - tmp[1])
        time += tmp[2]
        while len(program) >0 and program[0][1] <= time:
            heapq.heappush(heap, program.pop(0))
        
    answer[0] += time
    
    
    return answer