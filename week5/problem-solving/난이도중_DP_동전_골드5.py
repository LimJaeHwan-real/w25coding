# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084
import sys
read=sys.stdin.readline
t=int(read().strip())

for _ in range(t):
    n=int(read().strip())
    coins=list(map(int,read().strip().split()))
    goal=int(read().strip())
    
    dp=[0]*(goal+1)
    dp[0]=1
    for coin in coins:
        for money in range(coin, goal+1):
            dp[money] += dp[money - coin]
    

    print(dp[goal])

