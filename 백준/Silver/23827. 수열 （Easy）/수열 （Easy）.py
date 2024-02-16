n = int(input())

arr = list(map(int, input().split()))
s = sum(arr)
result =0

for i in arr:
    s -= i
    result = (result + i * s) % 1000000007
    
print(result)
