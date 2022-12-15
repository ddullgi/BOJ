for _ in range(3):
    s = str(input())
    _max = 1
    cnt = 1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            cnt+=1
        else:
            _max=max(cnt,_max)
            cnt=1
    _max = max(cnt, _max)
    print(_max)