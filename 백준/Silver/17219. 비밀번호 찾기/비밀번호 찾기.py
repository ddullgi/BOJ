N, M = map(int, input().split())
dict = {}
for _ in range(N):
    site, password = input().split()
    dict[site] = password
for _ in range(M):
    print(dict[input()])