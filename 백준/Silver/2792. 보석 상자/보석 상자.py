import math, sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = []
for _ in range(M):
	arr.append(int(input()))
 
def solution(l, r):
	n = 0xfffffff
	while l <= r:
		tmp = 0
		m = (l + r) // 2
		for i in arr:
			tmp += math.ceil(i / m)
		
		if tmp > N:
			l = m + 1
		else:
			r = m - 1
			n = min(n, m)
	return n
 
print(solution(1, max(arr)))