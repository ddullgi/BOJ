N = int(input())
arr = ['NO'] * (N + 4)
# SK 가 이기면 0 CY가 이기면 1
arr[1] = 'SK'
arr[2] = 'CY'
arr[3] = 'SK'
arr[4] = 'SK'
def game(n):
    sel = [4, 3, 1]
    if arr[n] != 'NO':
        return arr[n]
    for i in sel:
        num = game(n - i)
        if num == 'CY':
            arr[n] = 'SK'
            return 'SK'
    arr[n] = 'CY'
    return 'CY'

for j in range(5,N+1):
    game(j)

print(arr[N])