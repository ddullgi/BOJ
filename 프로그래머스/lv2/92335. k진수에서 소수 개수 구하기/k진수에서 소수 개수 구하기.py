def convert_iter(num, base):
    power = 0
    tmp = ''
    while num:
        tmp = str(num % base) + tmp
        num //= base
    return tmp

def check(num):
    for i in range(2, int(num**(1/2)) + 1):	
    	if num % i == 0:		
        	return False
    return True

def solution(n, k):
    answer = 0
    N = convert_iter(n, k)
    arr = list(map(str, N.replace("0", " ").split()))
    for i in arr:
        if i == "1":
            continue
        if check(int(i)):
            answer += 1
    return answer