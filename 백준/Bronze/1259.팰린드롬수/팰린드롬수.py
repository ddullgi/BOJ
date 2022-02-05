while True:
    N = str(input())
    if N == '0':
        break
    T = ''
    for i in N:
        T = i + T

    if N == T:
        print('yes')
    else:
        print('no')