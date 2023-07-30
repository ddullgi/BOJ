def change_num(arr, idx):
    arr[idx] = 1 - arr[idx]

def count_press(s, e):
    S_copy = s[:]
    count = 0

    for i in range(1, N):

        if S_copy[i - 1] == e[i - 1]:
            continue

        count += 1
        for j in range(i - 1, i + 2):
            if j < N:
                change_num(S_copy, j)

    if S_copy == e:
        return count
    else:
        return 1e9


N = int(input())
S = list(map(int, input()))
E = list(map(int, input()))

result = count_press(S, E)

S[0], S[1] = 1 - S[0], 1 - S[1]

result = min(result, count_press(S, E) + 1)
if result != 1e9:
    print(result)
else:
    print(-1)

