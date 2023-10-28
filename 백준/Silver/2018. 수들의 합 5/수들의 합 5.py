n = int(input())
start, end = 1, 1
cnt, total = 0, 1

while end != n:
    if total < n: 
        end += 1
        total += end
    elif total > n: 
        total -= start
        start += 1
    else: 
        cnt += 1
        end += 1
        total += end

print(cnt + 1) 