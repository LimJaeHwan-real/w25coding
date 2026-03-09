# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

import sys
from math import sqrt

read=sys.stdin.readline

n=read().strip()
arr=map(int,read().split())
result=0
def isprime(n):
    if n<2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

for i in arr:
    if isprime(i):
        result+=1

print(result)

