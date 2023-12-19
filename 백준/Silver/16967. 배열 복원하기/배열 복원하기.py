h, w, x, y = map(int, input().split())

answer = []
arr = []

for _ in range(h + x):
    arr.append(list(map(int, input().split())))

for i in range(h):
    answer.append(arr[i][:w])

for i in range(h):
    for j in range(w):
        if i+x < h and j + y < w:
            answer[i + x][j + y] -= answer[i][j]

for a in answer:
    print(" ".join(map(str, a)))