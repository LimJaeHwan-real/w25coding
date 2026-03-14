# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406
import sys
from collections import deque
read=sys.stdin.readline

arr1=deque([c for c in read().strip()])
arr2=[]
n=int(read().strip())


for _ in range(n):
    cmd=read().strip()
    if cmd[0]=='P':
        cmd,data=cmd.split()
        arr1.append(data)
    elif cmd[0]=="L":
        if arr1:
            arr2.append(arr1.pop())
    elif cmd[0]=="D":
        if arr2:
            arr1.append(arr2.pop())
    else:
        if arr1:
            arr1.pop()
    
arr1.extend(reversed(arr2))
print("".join(arr1))
            