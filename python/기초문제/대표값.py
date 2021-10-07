n = int(input())
scores = list(map(int, input().split()))

avg = int((sum(scores) / n) + 0.5)

minDiff = 214700000
maxScore = -214700000

for i in range(n):
    diffScore = abs(scores[i] - avg)
    if diffScore == minDiff:
        if scores[i] > maxScore:
            minDiff = diffScore
            maxScore = scores[i]
            minIndex = i

    elif diffScore < minDiff:
        minDiff = diffScore
        maxScore = scores[i]
        minIndex = i

print(avg, minIndex + 1, sep=' ')
