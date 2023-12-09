n = int(input())
arr = list(map(int,input().split()))

card = arr[:]
for i in range(n):
    for j in range(i):
        card[i] = max(card[i], card[i - j - 1] + arr[j])

print(card[n - 1])