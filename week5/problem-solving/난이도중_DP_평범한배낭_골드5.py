# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865
# import sys
# read=sys.stdin.readline

# 2차원배열 T:O(nk), S:O(nk)
# n,limit=map(int,read().strip().split())
# dp[i][j] : i번째 물건까지 고려 했을때 무게 j에서의 최댓값
# dp=[[0 for _ in range(limit+2)] for _ in range(n+2)]
# w,p=[0],[0]
# for _ in range(n):
#     wt,pt=map(int,read().strip().split())
#     w.append(wt)
#     p.append(pt)


# for num in range(1,n+1):
#     for weight in range(1,limit+1):
#         if weight>=w[num]:
#             dp[num][weight]=max(dp[num-1][weight], p[num]+dp[num-1][weight-w[num]])
#         else:
#             dp[num][weight]=dp[num-1][weight]
# print(dp[n][limit])

# 1차원배열 T:O(nk), S:O(k)
import sys
read=sys.stdin.readline

n,k=map(int,read().strip().split())
# dp[j] : 현재 물건까지 고려한 무게 j에서의 최댓값
dp = [0]*(k+1)

for i in range(n):
    w,v=map(int,read().strip().split())
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)

print(dp[k])
