import sys

a = int(sys.stdin.readline()) # sys를 이용해 빠른 입력 받기기
b = int(sys.stdin.readline())


def is_primenum(x): # 소수 검출 함수 정의
    '''
    약수들은 대칭적으로 짝을 이루기 때문에 자기 자신의 루트까지만 확인하면 됨됨
    '''
    for i in range(2, int(x**(1/2)) + 1): 
        if x % i == 0:
            return False
    return True


lst = [] # 소수들을 넣어줄 리스트 

for num in range(a,b+1):
    if num > 1:
        flag = False
        flag = is_primenum(num)
        if flag == True: # 소수면 lst에 추가
            lst.append(num)


# 소수가 없으면 -1 출력 
if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])

