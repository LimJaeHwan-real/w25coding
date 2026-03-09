# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157
from collections import Counter
import sys

read=sys.stdin.readline
dict_str=Counter(read().strip().lower())
mx=max(dict_str.values())


if sum( 1 for i in dict_str.values() if i==mx)>1:
    print("?")
else:
    print(max(dict_str,key=dict_str.get).upper())





