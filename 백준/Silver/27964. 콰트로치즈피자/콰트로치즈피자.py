N = int(input())
arr = set(input().split())
count = 0
for i in arr:
    if i[-6:] == "Cheese":
        count += 1

if count >= 4:
    print("yummy")
else:
    print("sad")