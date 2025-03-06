import sys

num = int(input())

lst = [sys.stdin.readline().strip() for i in range(num)] # sys를 이용해서 빠르게 단어 받기
lst = set(lst) # 중복 단어 제거

# lambda 를 이용해서 간단하게 구현 가능함
# 먼저 단어 길이로 정렬 하고 len(x) 이후에 길이가 같으면 사전순 정렬 
lst = sorted(lst, key=lambda x: (len(x), x)) 

for val in lst:
    print(val)
