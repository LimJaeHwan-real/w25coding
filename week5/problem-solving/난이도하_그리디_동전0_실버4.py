# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047
import sys
read=sys.stdin.readline

n,k=map(int,read().strip().split())
coins=[]
result=0

for _ in range(n):
    coins.append(int(read().strip()))
coins.sort(reverse=True)

for coin in coins:
    coin_num=k//coin
    if (coin_num)>0:
        result+=(coin_num)
        k=k%coin

print(result)

