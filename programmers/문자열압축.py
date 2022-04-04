def solution(s):
    answer = len(s)

    for size in range(1, len(s) // 2 + 1):
        count = 1
        compress = 0

        prev = s[:size]
        for i in range(size, len(s) + size, size):
            curr = s[i:i + size]
            if prev == curr:
                count += 1
            else:
                if count == 1:
                    compress += len(prev)
                else:
                    compress += size + len(str(count))
                prev = curr
                count = 1
        answer = min(answer, compress)

    return answer
