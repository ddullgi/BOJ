for test in range(int(input())):
    N, M = map(int, input().split())
    
    arr = [list(map(int,input().split())) for _ in range(N)]
    answer = [[] for _ in range(2)]
    
    for i in range(N):
        answer[0].append(sum(arr[i]))
        
    for i in range(N):
        answer[1].append(sum(arr[m][i] for m in range(N)))
        
    for _ in range(M):
        r1, c1, r2, c2, v = map(int, input().split())
        
        for i in range(r1 - 1, r2):
            answer[0][i] += (c2 - c1 + 1) * v
            
        for i in range(c1 - 1, c2):
            answer[1][i] += (r2 - r1 + 1) * v

    for i in range(2):
        print(*answer[i])