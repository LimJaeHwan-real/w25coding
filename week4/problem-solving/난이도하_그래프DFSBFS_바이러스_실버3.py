# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
import sys
from collections import deque
read=sys.stdin.readline
n=int(read().strip())
m=int(read().strip())

result=0
visited=[0]*(n+1)
board=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    u,v=list(map(int,read().strip().split()))
    board[u][v]=1
    board[v][u]=1

q=deque()
q.append(1)
visited[1]=1
while q:
    u=q.popleft()
    for v in range(1,n+1):
        if visited[v] or not board[u][v]:
            continue
        q.append(v)
        visited[v]=1
        result+=1

print(result)


















