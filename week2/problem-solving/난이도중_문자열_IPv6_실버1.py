# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107
import sys

#  ':' x 7 , '0000' x 8
# 어차피 사라진건 0이다

read=sys.stdin.readline
instr=read().strip()
result=''
arr=instr.split(":")
if arr[0]=='':
    arr=arr[1:]

if arr[-1]=='':
    arr=arr[:-1]

for i in arr:
    if i=='':
        result+=(9-len(arr))*'0000:'
    else:
        result+=i.zfill(4)+':'

print(result[:-1])











print(result)



      


      









      
      
    
# 1) ':' 7개 다있는 경우 -> 앞에 0만 채워 넣으면됨

# 2) "::" 가 있는 경우 7-(현재 ":" 갯수)+1 * "0000" 채워넣기

# 1) 2) 섞인 경우




















