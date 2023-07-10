from itertools import combinations

def solution(number):

    return sum([1 if sum(k) == 0 else 0 for k in combinations(number, 3)])