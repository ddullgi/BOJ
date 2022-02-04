min, max = map(int, input().split())

bool_list = [1] * (max - min + 1)

k = int(max ** 0.5)
for i in range(2, k + 1):
    square = i ** 2
    j = min//square
    if square * j < min:
        j += 1
    while square * j <= max:
        bool_list[square * j - min] = 0
        j += 1
print(sum(bool_list))
