# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251
import sys
read=sys.stdin.readline
dp=[[0]*1002 for _ in range(1002)]
str1=read().strip()
str2=read().strip()


for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        if str1[i-1]!=str2[j-1]:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        else:
            dp[i][j]=dp[i-1][j-1]+1
     
print(dp[len(str1)][len(str2)])