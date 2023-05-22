def dfs(K, dungeons, visit, l, count, arr):
    check = 0 
    for i in range(l):
        if visit[i] == 0 and dungeons[i][0] <= K:
            visit[i] = 1
            dfs(K - dungeons[i][1], dungeons, visit, l, count + 1, arr)
            visit[i] = 0
            check += 1
    
    if check == 0:
        arr.append(count)
    


def solution(k, dungeons):
    answer = -1
    arr = []
    l = len(dungeons)
    visit = [0] * l
    dfs(k, dungeons, visit, l, 0, arr)
    answer = max(arr)
    return answer