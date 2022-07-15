N = int(input())
books = {}
for _ in range(N):
    S = input()
    if books.get(S):
        books[S] += 1
    else:
        books[S] = 1

lst = list(books.items())
lst.sort(key=lambda x: (-x[1], x[0]))
print(lst[0][0])