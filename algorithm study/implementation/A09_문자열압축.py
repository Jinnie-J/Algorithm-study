def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        cnt = 1
        for j in range(step, len(s), step):
            if s[j:j + step] == prev:
                cnt += 1
            else:
                if cnt >= 2:
                    compressed += str(cnt) + prev
                else:
                    compressed += prev
                prev = s[j:j + step]
                cnt = 1
        if cnt >= 2:
            compressed += str(cnt) + prev
        else:
            compressed += prev
        answer = min(answer, len(compressed))
    return answer
