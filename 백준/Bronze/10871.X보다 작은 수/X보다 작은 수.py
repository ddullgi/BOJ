N, X = map(int, input().split())
T = list(map(int, input().split()))
for i in T:    
    if i < X:
        print(i,end = ' ')