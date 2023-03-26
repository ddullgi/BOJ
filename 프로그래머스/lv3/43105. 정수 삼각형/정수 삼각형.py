def solution(triangle):
    answer = 0
    l = len(triangle)
    for i in range(l - 1, -1, -1):
        if i == 0:
            answer = triangle[0][0]
        else:
            for j in range(0, i):
                triangle[i - 1][j] +=  max(triangle[i][j], triangle[i][j + 1])
    return answer