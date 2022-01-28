n, m = map(int, input().split())

def fun():
    if len(arr) == m:
        num = ''
        for i in arr:
            num = num + str(i) + ' '

        print(num[:-1])
        return
    else:
        for i in range(1,n + 1):
            if i not in arr:
                arr.append(i)
                fun()
                arr.pop()

arr = []
fun()