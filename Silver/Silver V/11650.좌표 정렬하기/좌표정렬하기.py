import sys

num = int(sys.stdin.readline().strip()) 

# 좌표 입력 받기
lst = [list(map(int, sys.stdin.readline().split())) for i in range(num)]


# 좌표의 x로 먼저 정렬 했다가 x가 같다면 Y를 기준으로 정렬 
lst = sorted(lst, key= lambda x : (x[0], x[1]))

# 출력 
for val in lst:
    print(*val)
