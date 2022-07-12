def check(text):
    L = len(text)
    D = 0
    while D < L - 1:
        step = 0
        Set = set()
        while step + D + 1 < L:
            D_pair = text[step] + text[step + D + 1]
            if D_pair in Set:
                return False
            else:
                Set.add(D_pair)
                step += 1
        D += 1
    return True

while True:
    T = input()
    if T == '*':
        break
    if check(T):
        result = ''
    else:
        result = 'NOT '
    print(f'{T} is {result}surprising.')
