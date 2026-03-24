# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725

import sys
from collections import deque
read=sys.stdin.readline
n=int(read())

board=[[] for _ in range(n+1)]

parent=[0]*(n+1)
q=deque()

for _ in range(n-1):
    u,v=map(int,read().split())

    board[u].append(v)
    board[v].append(u)

q.append(1)
parent[1]=-1

while q:
    cur=q.popleft()
    
    for adj in board[cur]:
        if parent[adj]==0:
            parent[adj]=cur
            q.append(adj)

for i in range(2,n+1):
    print(parent[i])  


















