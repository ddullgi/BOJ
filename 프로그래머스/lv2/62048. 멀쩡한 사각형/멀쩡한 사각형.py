def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(w,h):
    answer = 1
    x = gcd(w, h)
    ww = w // x
    hh = h // x
    cut = ww * hh - (ww - 1) * (hh - 1)
    answer = w * h - cut * x
    return answer