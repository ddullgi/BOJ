import sys, heapq

H = []
n = int(sys.stdin.readline())
for i in range(n):
	num = int(sys.stdin.readline())
	if num:
		heapq.heappush(H, (abs(num), num))
	else:
		if H:
			print(heapq.heappop(H)[1])
		else:
			print(0)