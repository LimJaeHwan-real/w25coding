# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819
import sys
from itertools import permutations
read=sys.stdin.readline

n=int(read())
org_arr=list(map(int,read().strip().split()))

perm=list(permutations(org_arr,n))
result=0
for arr in perm:
    result=max( result,sum( [abs(arr[i-1]-arr[i]) for i in range(1,n)] ) )
print(result)




# # 백트래킹 방법
# visited=[0]*n
# # index (1~n-1) 까지 양쪽 옆 요소와의 차를 통해 값을 얻을 수 있다
# result=0

# def ssum(arr):
#     sum=0
#     for i in range(1,n):
#         sum+=abs(arr[i-1]-arr[i])
#     return sum

# def re(arr):
#     global result
#     if len(arr)==n:
#         result=max(result,ssum(arr))
#         return
#     for i in range(n):
#         if not visited[i]:
#             visited[i]=1
#             re(arr+[org_arr[i]])
#             visited[i]=0


# re([])
# print(result)












































