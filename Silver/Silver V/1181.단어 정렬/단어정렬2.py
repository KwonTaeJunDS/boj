import sys

n = int(sys.stdin.readline().strip())

# set으로 중복 제거 
lst = set(sys.stdin.readline().strip() for i in range(n))

# 다시 리스트로 변환 
lst = list(lst)

# lambda를 이용한 정렬 
lst.sort(key = lambda x : (len(x), x))

for val in lst:
    print(val)
