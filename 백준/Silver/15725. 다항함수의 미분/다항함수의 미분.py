a = input().split("x")

if len(a) == 1:
    print(0)
elif a[0] == "":
    print(1)
elif a[0] == "-":
    print(-1)
else:
    print(a[0])