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
            if len(arr) == 0:
                arr.append(i)
                fun(k)
                arr.pop()
            elif arr[len(arr) - 1] > i:
                continue
            elif arr[len(arr) - 1] == i:
                arr.append(i)
                fun(k)
                arr.pop()
            else:
                arr.append(i)
                fun(k + 1)
                arr.pop()


arr = []
fun(1)