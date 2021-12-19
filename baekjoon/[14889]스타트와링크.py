from itertools import combinations

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arrRange = [x for x in range(n)]

minsum = 2147000000
team = set(range(0, n))

for teamA in combinations(arrRange, n // 2):
    teamB = list(team - set(teamA))
    sumA = 0
    sumB = 0
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            sumA += arr[teamA[i]][teamA[j]] + arr[teamA[j]][teamA[i]]
            sumB += arr[teamB[i]][teamB[j]] + arr[teamB[j]][teamB[i]]

    minsum = min(minsum, abs(sumA - sumB))
print(minsum)
