# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056
import sys
from collections import deque,defaultdict

read=sys.stdin.readline
n=int(read().strip())

# 작업 소요시간 /선행관계 작업들의 수 /선행 관계 작업 번호
graph=defaultdict(list)
q=deque()




