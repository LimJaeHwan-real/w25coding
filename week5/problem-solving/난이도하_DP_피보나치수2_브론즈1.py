# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748
import sys
read=sys.stdin.readline

dp=[-1]*100

dp[0]=0
dp[1]=1
n=int(read().strip())
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])