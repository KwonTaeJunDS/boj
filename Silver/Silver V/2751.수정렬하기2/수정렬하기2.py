import sys

num = int(sys.stdin.readline()) 

lst = [0 for _ in range(num)] # 0으로 리스트를 만들어 놓고

for i in range(num): # 인덱스로 접근해서 lst 생성성
    lst[i] = int(sys.stdin.readline())

lst.sort() # 정렬 후

# 프린트트
for val in lst: 
    print(val)
