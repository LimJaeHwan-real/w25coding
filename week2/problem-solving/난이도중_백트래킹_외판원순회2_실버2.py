# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

import sys
read=sys.stdin.readline

n=int(read().strip())
arr=[[0 for _ in range(n)] for _ in range(n)]
visited=[0]*n

for i in range(n):
    arr[i]=list(map(int,read().strip().split()))


mn=sys.maxsize
def sol(cnt,start,dist,history):
    global mn
    if cnt==(n-1) and arr[start][0]:
        mn=min(mn,dist+arr[start][0])
        print(history)
        return
    
    for i in range(n):
        if not visited[i] and arr[start][i]:
            visited[i]=1
            sol(cnt+1,i,dist+arr[start][i],history+[i])
            visited[i]=0

visited[0]=1
sol(0,0,0,[0])
print(mn)




