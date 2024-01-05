n, m = map(int, input().split())
li = list(map(int, input().split()))

st = set()
for i in range(m):
    st.add(li[i])
    for j in range(i + 1, m):
        st.add(li[i] + li[j])

dp = [-1] * (n + 1)
dp[0] = 0

for value in st:
    for i in range(n - value + 1):
        if dp[i] != -1:
            v = i + value
            if dp[v] == -1 or dp[v] > dp[i] + 1:
                dp[v] = dp[i] + 1

print(dp[-1])