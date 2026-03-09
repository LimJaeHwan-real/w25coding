# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914
import sys

read=sys.stdin.readline

n=int(read())

def hanoi(num,a, b ,c):
    if num==1:
        print(f"{a} {c}")
        return
    hanoi(num-1,a,c,b)
    print(f"{a} {c}")
    hanoi(num-1,b,a,c)

print(2**n-1)
if n<=20:
    hanoi(n,1,2,3)











    










