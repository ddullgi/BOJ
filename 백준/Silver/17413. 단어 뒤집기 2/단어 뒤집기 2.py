S = str(input())
save = ''
result = ''
state = False
for i in S:
    if state == True:
        if i == '>':
            state = False
        result += i
    else:
        if i == ' ':
            result += save[::-1] + ' '
            save = ''
        elif i == '<':
            state = True
            result += save[::-1]
            save = ''
            result += '<'
        else:
            save += i
if i != '>':
    result += save[::-1]

print(result)