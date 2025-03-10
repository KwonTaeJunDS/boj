import sys

num = int(sys.stdin.readline().strip())

# 나이하고 이름 입력받기 
lst = [list(sys.stdin.readline().split()) for i in range(num)]

for i in range(len(lst)): 
    lst[i][0] = int(lst[i][0]) # str 형태인 나이를 int로 바꿔줌
    lst[i].append(i) # 맨 뒤에 가입순을 추가함 

# 정렬 
lst = sorted(lst, key = lambda x: (x[0], x[2]))

for val in lst:
    print(*val[:2])
