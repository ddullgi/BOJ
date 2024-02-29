s = list(input())
cnt = s.count("a")
answer = 0xffffffffffff
l = 0

while l < len(s):
    r = l + cnt
    if r > len(s):
        tmp = s[l:len(s)] + s[:r-len(s)]
    else:
        tmp = s[l:r]
    answer = min(answer, tmp.count("b"))
    l += 1

print(answer)