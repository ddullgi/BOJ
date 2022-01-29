T = int(input())
for i in range(T):
    A = str(input())
    if A[0] == 'O':
        check = 1
        score = 1
    else:
        check = 0
        score = 0
    for j in range(1, len(A)):
        if A[j] == 'O' and A[j -1] == 'O':
            check += 1
            score += check
        elif A[j] == 'O':
            score += 1
            check = 1
    print(score)