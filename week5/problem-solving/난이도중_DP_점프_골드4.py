# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253
import sys
read=sys.stdin.readline
n,m=map(int,read().strip().split())
dp=[[float('inf')]* (int((2*n)**0.5)+2) for _ in range(n+1)]

# 못가는 돌 리스트
small_stones=set()

for _ in range(m):
    small_stones.add(int(read().strip()))

dp[1][0]=0

for i in range(2,n+1):
    if i in small_stones:
        continue
    for v in range(1,int((2*n)**0.5)+2):
        if i-v>=0:
            m=dp[i-v][v]
            if v-1>=0:
                m=min(m,dp[i-v][v-1])
            if v+1<=int((2*n)**0.5)+1:
                m=min(m,dp[i-v][v+1])
            
            dp[i][v]=m+1
           
if min(dp[n])>=float('inf'):
   print(-1)
else:
   print(min(dp[n]))













