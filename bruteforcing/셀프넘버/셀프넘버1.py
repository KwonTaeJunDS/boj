# 집합으로 모두 정의
lst = set(range(1, 10001))
flag = set()

# 셀프 넘버가 아닌 숫자를 모두 찾아서 flag에 저장 
for i in range(1, 10001):
    p = i + sum(map(int, str(i)))
    flag.add(p)

# 차집합으로 셀프 넘버 추출
lst -= flag

# 집합은 무작위라 정렬
lst = sorted(lst)

for val in lst:
    print(val)

