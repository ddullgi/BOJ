def solution(lottos, win_nums):
    ranking = [6, 6, 5, 4, 3, 2, 1]
    a = set(lottos)
    b = set(win_nums)
    min_n = len(a & b)
    unknown_n = 0
    for i in lottos:
        if i == 0:
            unknown_n += 1
    return [ranking[min_n + unknown_n],ranking[min_n]]