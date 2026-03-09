# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663
import sys

read=sys.stdin.readline
n=int(read().strip())
arr1=[0]*n   # 같은 열
arr2=[0]*2*n # 같은 대각선(좌하단 -> 우상단)
arr3=[0]*2*n # 같은 대각선(좌상단 -> 우하단)
result=0
def func(row):
   
   if row==n:
      global result
      result +=1
      return
   if row<n:
        for col in range(n):
            if arr1[col] or arr2[row+col] or arr3[row-col+n-1]:
                continue
            arr1[col]=1
            arr2[row+col]=1
            arr3[row-col+n-1]=1
            func(row+1)
            arr1[col]=0
            arr2[row+col]=0
            arr3[row-col+n-1]=0

func(0)
print("결과 ",result)
        

