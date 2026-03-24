# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724
# union find로도 풀 수 있다!!
# import sys
# from collections import deque,defaultdict

# read=sys.stdin.readline
# n,m=map(int,read().strip().split())
# graph=defaultdict(list)
# visited=[0]*(n+2)
# q=deque()
# for _ in range(m):
#     u,v=map(int,read().strip().split())
#     graph[u].append(v)
#     graph[v].append(u)

# result=0
# def bfs(start):
#     global graph,visited,q,result
#     if visited[start]:
#         return
#     result+=1
#     q.append(start)
#     visited[start]=1

#     while q:
#         node=q.popleft()    
#         for adj in graph[node]:
#             if not visited[adj]:
#                 visited[adj]=1
#                 q.append(adj)

# for i in range(1,n+1):
#     bfs(i)
# print(result)    

graph = {

    'A': ['B', 'C'],

    'B': ['D', 'E'],

    'C': ['F'],

    'D': ['G'],

    'E': ['G'],

    'G': ['H'],

    'H': ['F'],

  }

def dfs(graph, start):

    visited = []

    back_edges = set()

    stack = [start]

    while stack:

        node = stack.pop()

        if node not in visited:

            visited.append(node)
            for adj in graph.get(node,[]):
                if adj not in visited:
                    stack.append(adj)
                else:
                    back_edges.add((node,adj))
        else:
            continue

    return visited, sorted(list(back_edges))

visited,back=dfs(graph,'A')
print(back)