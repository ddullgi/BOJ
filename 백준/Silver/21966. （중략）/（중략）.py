def solution(S, N):
    if N <= 25:
        return S

    front, mid, back = S[:11], S[11:-11], S[-11:]
    count = 0
    for i in mid[1:-1]:
        if i == ".":
            count += 1

    if count:
        return front[:9] + "......" + back[-10:]
    else:
        return front + "..." + back

N = int(input())
S = input()

print(solution(S, N))