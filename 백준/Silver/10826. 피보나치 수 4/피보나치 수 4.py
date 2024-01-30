import sys
sys.setrecursionlimit(0xfffffff)
n = int(input())
dp = [0 for i in range(10001)]

def fibo(n):
    if(dp[n] != 0): 
        return dp[n]
    
    if(n == 0): 
        return 0
    
    if(n == 1): 
        return 1
    
    dp[n] = fibo(n-1) + fibo(n-2)
    
    return dp[n]
    
print(fibo(n))