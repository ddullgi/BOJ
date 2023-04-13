import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
Q = deque()
now = list(map(int, input().split()))
answer = []

for i in range(N):

    # 1 나보다 큰 데이터 삭제 하기
    while Q and Q[-1][0] > now[i]:
        Q.pop()

    Q.append((now[i], i))

    # 2 슬라이딩 윈도우 벗어난 항목 삭제
    if Q[0][1] <= i - L:
        Q.popleft()

    answer.append(Q[0][0])

print(*answer)