n, m = map(int, input().split())

def fun(k):
    if len(arr) == m:
        num = ''
        for i in arr:
            num = num + str(i) + ' '

        print(num[:-1])
        return
    else:
        for i in range(k,n + 1):
            if i not in arr:
                arr.append(i)
                k += 1
                fun(k)
                arr.pop()

arr = []
fun(1)