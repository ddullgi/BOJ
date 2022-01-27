N = int(input())
score = []
for s in range(N):
    score.append(int(input()))

result = 0
for j in range(len(score)-2,-1,-1):
    if score[j] >= score[j+1]:
        result += (score[j] -score[j+1] + 1)
        score[j] = score[j+1] - 1

print(result)