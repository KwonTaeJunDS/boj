import sys
w, h = map(int, sys.stdin.readline().rstrip().split())

a_list = []
b_list = []
answer_list = []

for i in range(w):
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    a_list.append(lst)

for i in range(w):
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    b_list.append(lst)

for i in range(w): # 바로 프린트해줘야 원하는 출력값 받을 수 있음음
    for j in range(h):
        print(a_list[i][j] + b_list[i][j], end=' ')
    print()
