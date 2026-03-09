# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

import sys

read=sys.stdin.readline
arr=[]
for _ in range(9):
    arr.append(int(read()))
print(max(arr))
print(arr.index(max(arr))+1)



