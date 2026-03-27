# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904
import sys
read=sys.stdin.readline

# 00과 1만으로
# n=1 -> 1
# n=2 -> 00,11
# n=3 -> 001, 100, 111
# n=4 -> 0011, 0000, 1001, 1100, 1111
dp=[0,1,2]
n= int(read().strip())
for i in range(3,n+1):
    dp.append((dp[i-1]+dp[i-2])%15746)

print(dp[n])