result = 0


def nqueen(board, n ,col):
    global result
    
    if col == n:
        result += 1
        return
    
    for row in range(n):
        board[col] = row
        
        for x in range(col):
            # 열이 같으면 돌아
            if board[x] == row:
                break
            # 대각선이 겹치면 돌아가
            if abs(board[x] - row) == col - x:
                break
        # 중복이 없으면 더 들어가
        else: 
            nqueen(board, n, col + 1)
    
            
    

def solution(n):
    Q = [0] * n
    nqueen(Q, n, 0)
    return result


























# def nqueen(queen, n, row):
#     count = 0
    
#     if n == row:
#         return 1
    
#     # 가로로 한번만 진행
#     for col in range(n):
#         queen[row] = col
        
#         # 앞의 것과 비교
#         for x in range(row):
#             if queen[x] == queen[row]:
#                 break
#             if abs(queen[x]-queen[row]) == row-x:
#                 break
#         else:
#             count += nqueen(queen, n, row+1)
#     return count

# def solution(n):
#     queen = [0] * n
#     return nqueen(queen, n, 0)