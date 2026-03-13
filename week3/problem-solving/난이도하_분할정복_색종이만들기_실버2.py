# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630
import sys
read=sys.stdin.readline
WHITE='0'
BLUE='1'

n=int(read().strip())
board=[]
for i in range(n):
    board.append(read().strip().split())

def is_all(y,x,m,color):
    for i in range(y,y+m):
        for j in range(x,x+m):
            if board[i][j]!=color:
                return False
    return True
    
    
    
blue_cnt=0
white_cnt=0
def sol(y,x,m):
    global blue_cnt,white_cnt
    if is_all(y,x,m,WHITE):
        white_cnt+=1
        return
    if is_all(y,x,m,BLUE):
        blue_cnt+=1
        return
    half=m//2
    sol(y,x,half)
    sol(y,x+half,half)
    sol(y+half,x,half)
    sol(y+half,x+half,half)
   
sol(0,0,n)
print(white_cnt)    
print(blue_cnt)

    
    
