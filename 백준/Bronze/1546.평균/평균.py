import math
N = int(input())
scores = list(map(int, input().split()))
print(sum(scores)/N*100/max(scores))