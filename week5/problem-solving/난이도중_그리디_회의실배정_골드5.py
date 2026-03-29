# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931
import sys
read=sys.stdin.readline
result=1
meetings=[]

n=int(read().strip())
for _ in range(n):
    s,e=map(int,read().strip().split()) 
    meetings.append((s,e))

meetings.sort(key=lambda x:(x[1],x[0]))
prev=meetings[0]    
for meet in meetings[1:]:
    if meet[0]>=prev[1]:
        result+=1
        prev=meet

print(result)