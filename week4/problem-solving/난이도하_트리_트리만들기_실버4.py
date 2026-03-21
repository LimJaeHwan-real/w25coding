# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244
import sys
from collections import defaultdict
read=sys.stdin.readline
n,m=list(map(int,read().rstrip().split()))


for i in range(n-m+1):
    print(i,i+1)

for i in range(n-m+2,n):
    print(1,i)

