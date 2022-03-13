from itertools import combinations

# 소수 판별 함수
def get_primes(n):
    primes = []

    for i in range(2, n):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


def solution(n):
    primes = get_primes(n)

    # 3개의 소수 조합하여 n과 같은지 판별
    return [sum(c) for c in combinations(primes, 3)].count(n)
