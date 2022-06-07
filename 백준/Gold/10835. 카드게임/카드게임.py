N = int(input())
left_cards = tuple(map(int, input().split()))
right_cards = tuple(map(int, input().split()))
max_score = [[0]*(N+1) for _ in range(N+1)]

for l in range(N-1, -1, -1):
    for r in range(N-1, -1, -1):
        if right_cards[r] < left_cards[l]:
            max_score[l][r] = max_score[l][r+1]+right_cards[r]
        else:
            max_score[l][r] = max(max_score[l+1][r+1], max_score[l+1][r])

print(max_score[0][0])