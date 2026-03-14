# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828
import sys

read=sys.stdin.readline

n=int(read().strip())
stack=[]
for _ in range(n):
    #print(stack)
    cmd=read().strip()
    if cmd=="pop":
        if stack:  
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif cmd=="size":
        print(len(stack))
    elif cmd=="empty":
        print(1 if not stack else 0)
    elif cmd=="top":
        # top
        print(-1 if not stack else stack[-1])
    else:
        cmd,val=cmd.split()
        val=int(val)
        stack.append(val)
