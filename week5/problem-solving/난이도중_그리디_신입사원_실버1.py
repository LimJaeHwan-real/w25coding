# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946
import sys
read=sys.stdin.readline

t=int(read().strip())

for _ in range(t):
    arr=[]
    result=1
    n=int(read().strip())
    for _ in range(n):
        paper,interview=map(int,read().strip().split()) 
        arr.append((paper,interview))


    arr.sort(key=lambda x:x[0])

    minimum_interview=arr[0][1]

    for paper,interview in arr[1:]:

        if interview<minimum_interview:
            result+=1
            minimum_interview=interview
    
    print(result)

