def solution(numbers, hand):
    answer = ''
    nowL = 10
    nowR = 12

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            nowL = n
        elif n in [3, 6, 9]:
            answer += 'R'
            nowR = n
        else:
            n = 11 if n == 0 else n

            absL = abs(n - nowL)
            absR = abs(n - nowR)

            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer += 'R'
                nowR = n
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer += 'L'
                nowL = n
            else:
                if hand == 'left':
                    answer += 'L'
                    nowL = n
                else:
                    answer += 'R'
                    nowR = n

    return answer
