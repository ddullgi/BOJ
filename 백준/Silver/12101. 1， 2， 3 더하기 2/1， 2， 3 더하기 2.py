n, k = map(int, input().split())

def solution(x, answer):
    global cnt
    if x > n:
        return
    if n == x:
        cnt += 1
        if cnt == k:
            print("+".join(answer))
            exit()
    for i in (1, 2, 3):
        answer.append(f"{i}")
        solution(x + i, answer)
        answer.pop()

cnt = 0
solution(0, [])
print(-1)
