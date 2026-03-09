# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344
import sys

read=sys.stdin.readline

t=int(read())
for _ in range(t):
    n,*students=list(map(int,read().split()))
    avg=sum(students)/n
    up=[1 for score in students if score>avg ]
    percent=round(sum(up)/n*100,3)
    print(f'{percent:.3f}%')





