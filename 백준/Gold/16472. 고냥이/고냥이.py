n = int(input())
string = input()

dic = {}
answer = front = 0

for idx in range(len(string)):
    if dic.get(string[idx]):
        dic[string[idx]] += 1
    else:
        dic[string[idx]] = 1

    while len(dic) > n:
        dic[string[front]] -= 1

        if dic[string[front]] == 0:
            del dic[string[front]]
        front += 1

    answer = max(answer, idx - front + 1)

print(answer)