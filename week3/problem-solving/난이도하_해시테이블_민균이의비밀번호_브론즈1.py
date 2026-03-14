# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933
import sys

def sol():
    read=sys.stdin.readline
    n=int(read().strip())
    arr=[]

    for _ in range(n):
        word=read().strip()
        arr.append(word)
        if word==word[::-1] or word[::-1] in arr:
            print(len(word),word[len(word)//2])
            return
       
sol()
