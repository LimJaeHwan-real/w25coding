# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470
# 정렬 후 min<=x<=max 까지 중 이분탐색???

import sys

read=sys.stdin.readline
n=int(read().rstrip())
arr=list(map(int,read().rstrip().split()))

# 1. 투포인터
# arr.sort()

# left=0
# right=len(arr)-1
# mn_abs=sys.maxsize
# result=[0,0]

# while left<right:
#     sum=arr[left]+arr[right]
#     if abs(sum)<mn_abs:
#         result=[arr[left],arr[right]]
#         mn_abs=abs(sum)
#     if sum==0:
#         break
#     if sum<0:
#         left+=1
#     else:
#         right-=1


# print(result[0],result[1])

# 2. 이분탐색
mn_val=float('inf')
arr.sort()
for i in range(n-1):
    current=arr[i]
    target=-current
    left=i+1
    right=n-1
    
    while left<=right:
        mid=(left+right)//2
        sum_val=current+arr[mid]
        
        if abs(sum_val)<min_val:
            min_val=abs(sum_val)
            result=(current,arr[mid])
        
        if sum_val<0:
            left=mid+1
        else:
            right=mid-1

print(result[0],result[1])

























