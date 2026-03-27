# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541
import sys
read=sys.stdin.readline

input_str=read().strip().split('-')

result=sum(map(int,input_str[0].split('+')))

for s in input_str[1:]:
    result-=sum(map(int,s.split('+')))

print(result)