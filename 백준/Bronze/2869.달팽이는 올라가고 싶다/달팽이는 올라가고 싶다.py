a, b, v = map(int, input().split())
x = 0
if (v-b) % (a-b):
    x = int((v-b) // (a-b)) + 1
else:
    x = int((v-b) // (a-b))
print(x)