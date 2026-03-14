# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164
import sys
from collections import deque
read=sys.stdin.readline
n= int(read().strip())
arr=deque([i for i in range(1,n+1)])

while len(arr)>1:
    if arr:
        arr.popleft()
    if arr:
        data=arr.popleft()
        arr.append(data)
print(arr[0])

