def solution(board, skill):
    answer = 0
    m, n = len(board), len(board[0])
    acc = [([0] * (n + 1)) for _ in range(m + 1)]
    
    for s in skill:
        t, r1, c1, r2, c2, degree = s
        damage = -degree if t == 1 else degree
        acc[r1][c1] += damage
        acc[r1][c2 + 1] -= damage
        acc[r2 + 1][c1] -= damage
        acc[r2 + 1][c2 + 1] += damage
        
    for j in range(m):
        for i in range(1, n):
            acc[j][i] += acc[j][i - 1]
            
    for i in range(n):
        for j in range(1, m):
            acc[j][i] += acc[j - 1][i]
            
    for j in range(m):
        for i in range(n):    
            board[j][i] += acc[j][i]
            if board[j][i] > 0:
                answer += 1

    return answer