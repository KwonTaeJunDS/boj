import sys


n = int(sys.stdin.readline().strip())

# 100 x 100의 흰 도화지 생성 
paper = [[0 for i in range(100)] for i in range(100)]

# x,y 좌표 받기 
cor = [list(map(int, sys.stdin.readline().strip().split())) for i in range(n)]

# 좌표를 돌면서 
for x, y in cor:
    for i in range(10):
        for j in range(10): # 가로, 세로 1로 칠하기 
            paper[x+i][y+j] = 1 


# 1있는 부분만 다 더하면 검은 영역의 넓이 나옴 
print(sum(sum(row) for row in paper)) 



