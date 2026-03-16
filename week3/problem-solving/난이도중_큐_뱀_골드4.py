# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190
import sys
from collections import deque

read=sys.stdin.readline
n=int(read().rstrip())
board=[[0 for _ in range(n)] for _ in range(n)]
apple_board=[[0 for _ in range(n)] for _ in range(n)]
q=deque() # 뱀이 현재 이동하고 있는 좌표 정보
rot_q=deque() # [x초후, 회전] L 왼쪽 회전, D 오른쪽회전

apple_cnt=int(read().rstrip())
right_rot=[[0,1],[1,0],[0,-1],[-1,0]]
left_rot=[[0,1],[-1,0],[0,-1],[1,0]]
cur=[0,0]
cur_dir=[0,1]
sum_second=0
def check_wall_mybody(board,r,c):
    # wall
    if r<0 or r>=n or c<0 or c>=n:
        return False
    # mybody 방문곳이면 board 1
    if board[r][c]==1:
        return False
    
    return True
def rotate(dir_c):# L 왼쪽 회전, D 오른쪽회전
    global left_rot,right_rot,cur_dir
    if dir_c=="L":
        idx=left_rot.index(cur_dir)
        idx=(idx+1)%len(left_rot)
        cur_dir=left_rot[idx]
    else:
        idx=right_rot.index(cur_dir)
        idx=(idx+1)%len(right_rot)
        cur_dir=right_rot[idx]


for _ in range(apple_cnt):
    r,c=list(map(int,read().rstrip().split()))
    r-=1
    c-=1
    apple_board[r][c]=1

snake_cnt=int(read().rstrip())
for _ in range(snake_cnt):
    s,d=read().rstrip().split()
    s=int(s)
    rot_q.append([s,d])

board[0][0]=1
q.append(cur[:])
while True:
    
    cur[0]+=cur_dir[0]
    cur[1]+=cur_dir[1]
    if not check_wall_mybody(board,cur[0],cur[1]):
        print(sum_second+1)
        break

    # 1. 현재위치 방문 (방문표시)
    board[cur[0]][cur[1]]=1
    # 2. 큐에 넣기
    q.append(cur[:])
    # 3. 사과 있다면 사과 없어지고 큐에서 빼지 않는다
    if apple_board[cur[0]][cur[1]]:
        apple_board[cur[0]][cur[1]]=0
    else:
    # 4. 사과 없다면 큐에서 빼고 방문표시를 지운다
        if q:
            dr,dc=q.popleft()
            board[dr][dc]=0
    # 5. 초를 늘린다
    sum_second+=1
    # 6. rot_q 체크해서 제일 앞의 요소의 초와 비교해서 sum_second 경과시간되면 회전    
    if rot_q:
        alarm_sec,dir_c=rot_q[0]
        if sum_second==alarm_sec:
            rotate(dir_c)
            rot_q.popleft()

