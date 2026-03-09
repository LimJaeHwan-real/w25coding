# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675
import sys

read=sys.stdin.readline

t=int(read())

for _ in range(t):
    n,s=read().split()
    n=int(n)
    print(''.join([c*n for c in s]))