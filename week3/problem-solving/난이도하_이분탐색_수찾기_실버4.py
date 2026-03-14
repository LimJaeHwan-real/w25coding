# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

import sys
read=sys.stdin.readline
n=int(read().strip())
arr=list(map(int,read().strip().split()))
m=int(read().strip())
target_arr=list(map(int,read().strip().split()))



def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return 1
        if arr[mid]<target:
            left=mid+1
        else:
            right=mid-1

    return 0

arr.sort()

for i in target_arr:
    print(binary_search(arr,i))
    