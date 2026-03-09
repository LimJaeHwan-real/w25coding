# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020
from math import sqrt
import sys

read=sys.stdin.readline

def is_prime(n):
    """
    소수 판별
    
    Args:
        n: 판별할 양의 정수
    
    Returns:
        소수이면 True, 아니면 False
    """
    # TODO: 소수 판별 구현
    # n이 2보다 작으면 False
    # 2부터 sqrt(n)까지 나누어 떨어지는지 확인    
    # 3부터 sqrt(n)까지 홀수만 확인
    if n<2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

t=int(read().strip())
while t>0:
    t-=1
    i=(int(read().strip()))
    for j in range(i//2,-1,-1):
        if is_prime(j) and is_prime(i-j):
            if j<(i-j):
                print(j,i-j)
            else:
                print(j,i-j)
            break
            
    
