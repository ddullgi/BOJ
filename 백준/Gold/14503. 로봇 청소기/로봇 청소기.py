N, M = map(int, input().split())
r, c, d = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

# 왼쪽 방향 초기화
left = 0

# 0: 북, 1: 동, 2: 남, 3: 서
dx = [0,  1, 0, -1]
dy = [-1, 0, 1,  0]

# 처음 위치는 청소함
cnt = 1
# 청소한 위치는 -1로 수정
maze[r][c] = -1

# 청소한 방향 갯수 저장
clean_cnt = 0

#청소 메커니즘 작성
while True:
    # c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    if clean_cnt == 4:
        clean_cnt = 0
        back = (d + 2) % 4
        # d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
        if maze[r + dy[back]][c + dx[back]] == 1:
            break
        else:
            r += dy[back]
            c += dx[back]
            continue

    # 왼쪽 방향 설정
    left = (d + 3) % 4
    d = left
    # a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    if maze[r + dy[left]][c + dx[left]] == 0:
        r += dy[left]
        c += dx[left]
        maze[r][c] = -1
        cnt += 1
        clean_cnt = 0
    # b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    elif maze[r + dy[left]][c + dx[left]] != 0:
        clean_cnt += 1
        continue

print(cnt)