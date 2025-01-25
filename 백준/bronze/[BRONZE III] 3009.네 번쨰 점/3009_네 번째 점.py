from collections import Counter

lst = []
for i in range(3): # 세 개의 좌표 입력력
    coor = list(map(int, input().split()))
    lst.append(coor)

x_list = []
y_list = []
for i in range(3): # x축과 y축 좌표 분리리
    x_list.append(lst[i][0])
    y_list.append(lst[i][1])

# 리스트 안의 요소 세기기
x_counts = Counter(x_list)
y_counts = Counter(y_list)

for e, c in x_counts.items(): # for문 돌면서 count가 1이면 한번만 나온 값이니 그 요소 print
    if c == 1:
        print(e, end=' ')
for e, c in y_counts.items():
    if c == 1:
        print(e)
