def quad(arr, x, y, n, answer):
    check = arr[x][y]
    for i in range(x, x+ n):
        for j in  range(y, y + n):
            if check != arr[i][j]:
                check = -1
                break
    
    if check == -1:
        n = n // 2
        quad(arr, x, y, n, answer)
        quad(arr, x + n, y, n, answer)
        quad(arr, x, y + n, n, answer)
        quad(arr, x + n, y + n, n, answer)
    elif check == 1:
        answer[1] += 1
    else:
        answer[0] += 1
        
def solution(arr):
    answer = [0, 0]
    n = len(arr)
    quad(arr, 0, 0, n, answer)
    return answer