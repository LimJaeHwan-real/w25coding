# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629
import sys
read=sys.stdin.readline
a,b,c=list(map(int,read().strip().split()))

def sol(base,exp,div):
    if exp==1:
        return base%div
    val=sol(base,exp//2,div)%div

    if exp%2==0:
        return val*val%div
    else:
        return base*val*val%div

print(sol(a,b,c))
    

