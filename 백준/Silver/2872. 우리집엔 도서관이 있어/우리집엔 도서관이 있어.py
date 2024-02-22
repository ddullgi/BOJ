N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

m = max(arr)

idx = arr.index(m)
answer = len(arr) - idx - 1

for book in arr[:idx][::-1]:
    if book == m - 1:
        m = book
    else:
        answer += 1
        
print(answer)