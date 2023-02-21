stack = []
dict = {}

for _ in range(int(input())):
    stack.append(input())

for string in stack:
    for i in range(len(string)):
        if string[i] in dict:
            dict[string[i]] += 10 ** (len(string) - i - 1)
        else:
            dict[string[i]] = 10 ** (len(string) - i - 1)


array = list(dict.values())
array.sort(reverse=True)

result = 0
num = 9
for j in array:
    result += j * num
    num -= 1
print(result)