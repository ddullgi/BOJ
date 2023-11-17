function solution(n, money) {
    const dp = Array(n + 1).fill(0)
    dp[0] = 1
    
    for(cost of money) {
        for(let i = cost; i <= n; i++) {
            dp[i] += dp[i - cost]
        }
    }
    
    return dp[n];
}