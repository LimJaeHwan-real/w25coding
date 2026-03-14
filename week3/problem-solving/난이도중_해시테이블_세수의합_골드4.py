# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295
import sys
read=sys.stdin.readline
n=int(read().rstrip())  
arr=[]

for _ in range(n):
    arr.append(int(read().rstrip()))

arr.sort()

sum_arr=set()
for x in arr:
    for y in arr:
        sum_arr.add(x+y)

def sol():
    global answer
    for k in range(n-1,-1,-1):
        for z in range(k+1):
            if (arr[k]-arr[z]) in sum_arr:
                answer=arr[k]
                return

answer=0

sol()
print(answer)