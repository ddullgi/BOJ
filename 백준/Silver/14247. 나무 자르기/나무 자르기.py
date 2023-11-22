N = int(input())                        
h = list(map(int, input().split()))     
speed = list(map(int,input().split())) 

arr = []
total = 0

for i in range(N):                  
    arr.append([h[i], speed[i]])

arr.sort(key = lambda x:x[1])       

for i in range(N):
    total += arr[i][0] + arr[i][1] * i

print(total)