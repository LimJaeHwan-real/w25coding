# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260
import sys
from collections import deque

read=sys.stdin.readline
n,m,start=map(int,read().strip().split())
graph=[[] for _ in range(n+2)]
dfs_arr=[]
bfs_arr=[]
for _ in range(m):
    u,v=map(int,read().strip().split())
    graph[u].append(v)
    graph[v].append(u)
    graph[u].sort()
    graph[v].sort()

def dfs():
    global dfs_arr
    stack=[]
    visited=[0]*(n+2)
    stack.append(start)
    
    
    while stack:
        node=stack.pop()
        if visited[node]:
            continue
        visited[node]=1
        dfs_arr.append(node)
        stack.extend(reversed(graph[node]))

def bfs():
    global bfs_arr
    q=deque()
    visited=[0]*(n+2)
    q.append(start)
    visited[start]=1

    while q:
        node=q.popleft()
        bfs_arr.append(node)
        for adj in graph[node]:
            if not visited[adj]:
                visited[adj]=1
                q.append(adj)
                        

dfs()
bfs()

print(*dfs_arr)
print(*bfs_arr)          

