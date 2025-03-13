import sys

num = int(sys.stdin.readline().strip())

lst = []

for i in range(num): # 좌표 받기기
    cor = list(map(int, sys.stdin.readline().strip().split()))
    lst.append(cor)

# y좌표를 기준으로 증가하는 순으로, y좌표가 같ㅌ으면 x좌표가 증가하는 순으로 정렬 
lst = sorted(lst, key=lambda x : (x[1], x[0]))

for val in lst:
    print(*val)
