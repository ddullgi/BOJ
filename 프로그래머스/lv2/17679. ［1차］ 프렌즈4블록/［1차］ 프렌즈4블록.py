def delete_square(board):
    m = len(board[0])
    n = len(board)
    for j in range(m):
        i = n - 1
        while i >= 0:
            if board[i][j] != "#":
                i -= 1
            else:
                board[i][j] = "@"
                for k in range(i, 0, -1):
                    board[k][j], board[k - 1][j] = board[k - 1][j], board[k][j]
    
    
                

def check_square(board, check_list):
    square = ((0, 1), (1, 0), (1, 1))
    X_list = set()
    count = 0
    for y, x in check_list:
        friends = board[y][x]
        if friends == "@":
            continue
        check = 1
        for dy, dx in square:
            if friends != board[y + dy][x + dx]:
                check = 0
                break
        
        if check == 1:
            X_list.add((y, x))
            for dy, dx in square:
                X_list.add((y + dy, x + dx))
    for y, x in X_list:
        board[y][x] = "#"
        count += 1
    
    if count == 0:
        return 0
    else:
        delete_square(board)
        count += check_square(board, check_list)
    
    return count
    

def solution(m, n, board):
    answer = 0
    new_board = [[j for j in i] for i in(board)]
    check_list = [(i, j) for i in range(m - 1) for j in range(n - 1)]
    answer = check_square(new_board, check_list)
    return answer