import sys
input = sys.stdin.readline

for i in range(int(input())):
    n , k = map(int, input().split())
    num = list(map(int, input().split()))
    num.sort()

    _max = 0xffffffff
    for j in range(n):
        l = j + 1
        r = n - 1
        while(l <= r):
            mid = (l + r) // 2
            s = num[j] + num[mid]
            if(s > k):
                r = mid - 1
            else:
                l = mid + 1
            if(abs(k - s) < _max):
                cnt = 1
                _max = abs(k - s)
            elif(abs(k - s) == _max):
                cnt += 1
    print(cnt)