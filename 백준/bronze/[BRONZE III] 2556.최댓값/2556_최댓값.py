lst = []

for i in range(9): # 이중 리스트 생성
    in_list = list(map(int, input().split()))
    lst.append(in_list)

answer = -1 # 최대값 갱신을 위한 값
index = [] 좌표 추출을 위한 index 리스트
for i in range(len(lst[:])):
    for j in range(len(lst[0])):
        if answer <= lst[i][j]:
            answer = lst[i][j]
            index = []
            index.append(i+1)
            index.append(j+1)

            

if answer == -1: # 만약 0값이 전부 들어온다면
    answer = 0
    print(answer)
    print(0, 0)
else:
    print(answer)
    print(index[0], index[1])  



############################################ GPT 코드
# 최대값과 좌표를 초기화
max_value = -1
max_row, max_col = 0, 0

for i in range(9):
    # 한 줄씩 입력받아 바로 처리
    row = list(map(int, input().split()))
    for j in range(9):
        if row[j] > max_value:
            max_value = row[j]
            max_row = i + 1  # 1-based index
            max_col = j + 1  # 1-based index

# 결과 출력
if max_value == -1:
  max_value = 0
  print(max_value)
  print(max_row, max_col)
else:
  print(max_value)
  print(max_row, max_col)
