T = int(input())
start = 0
end = T
while start <= end:
    mid = (start+end)//2
    if mid**2 == T:
        # print(mid)
        break
    elif mid**2 > T:
        end = mid - 1
    else:
        start = mid + 1
print(mid)