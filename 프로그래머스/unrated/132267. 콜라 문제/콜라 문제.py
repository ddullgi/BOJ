def solution(a, b, n):
    answer = 0
    while n >= a:
        plus = n // a * b
        n = n % a + plus
        answer += plus

    return answer