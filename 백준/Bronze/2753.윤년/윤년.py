year = int(input())

if year % 4:
    print(0)
else:
    if year % 400 == 0 or year % 100:
        print(1)
    else:
        print(0)