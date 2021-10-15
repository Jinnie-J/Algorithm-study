
# arr 배열에 words 원소 하나씩 추가하여, 길이 K가 넘어갈 시 단어 길이만큼 다시 pop() 해준 후 answer+1 해주었다.
def solution(K, words):
    answer = 0
    arr = []
    i = 0
    while i < len(words):
        for x in words[i]:
            arr.append(x)
        arr.append(' ')
        if len(arr) > K + 1:
            for j in range(len(words[i])):
                arr.pop()
            i -= 1
            answer += 1
            arr = []
        i += 1
    return answer + 1


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

print("solution 함수의 반환 값은", ret, "입니다.")
