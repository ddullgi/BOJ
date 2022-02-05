import sys
T = int(sys.stdin.readline())

dic = []
for i in range(T):
    dic.append(str(input()))

dic = list(set(dic))
dic.sort()
dic.sort(key=len)
for i in dic:
    print(i)
