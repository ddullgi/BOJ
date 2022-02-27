N, K = map(int, input().split())
dic = {}
for _ in range(N):
    sex, grade = map(int, input().split())
    try:
        dic[f'{grade}학년{sex}'] += 1
    except:
        dic[f'{grade}학년{sex}'] = 1

result = 0
for i in dic.values():
    result += i//K
    if i % K:
        result += 1
print(result)