# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
import sys
from collections import deque

def sol():
    read=sys.stdin.readline

    n=int(read().strip())
    board=[]
    visited=[[0]*n for _ in range(n)]
    for _ in range(n):
        board.append(list(map(int,read().strip().split())))

    q=deque()
    q.append([0,0])
    visited[0][0]=1
    def check(r,c):
        if r<0 or r>=n or c<0 or c>=n:
            return False
        
        if visited[r][c]:
            return False
        return True

    while q:
        cur=q.popleft()
        r,c=cur
        if board[r][c]==-1:
            print("HaruHaru")
            return 0
        dist=board[r][c]
        # 오른쪽
        nr,nc=r,c+dist
        if check(nr,nc):
            visited[nr][nc]=1
            q.append([nr,nc])
        # 아랫쪽
        nr,nc=r+dist,c
        if check(nr,nc):
            visited[nr][nc]=1
            q.append([nr,nc])
        
    print("Hing")
    return 0

sol()
    