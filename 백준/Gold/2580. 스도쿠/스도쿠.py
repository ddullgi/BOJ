def main(sudoku):
    def check_num(i, j):
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        square_y = i // 3 * 3
        square_x = j // 3 * 3
        square_area = sum([sudoku[r][square_x:square_x + 3] for r in range(square_y, square_y + 3)], [])

        row = set(sudoku[i])
        col = set([c[j] for c in sudoku])
        square = set(square_area)
        total_check = row | col | square
        total_num = set(nums)
        return list(total_num - total_check)


    def solution(idx):
        if idx == len(points):
            for line in sudoku:
                print(*line)
            exit(0)

        r, c = points[idx]
        nums = check_num(r, c)

        for x in nums:
            sudoku[r][c] = x
            solution(idx + 1)
            sudoku[r][c] = 0

    points = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                points.append((i, j))

    solution(0)

sudoku = [list(map(int, input().split())) for _ in range(9)]
main(sudoku)