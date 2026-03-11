import sys

n, m = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))


temp = 0 # 누적합을 위한 변수 선언
sum_lst = [0] # 누적합 저장 리스트 맨 첫번째는 0을로 해야 계산 편함

for val in lst:
    temp += val
    sum_lst.append(temp)


for c in range(m):
    i, j = map(int, sys.stdin.readline().split())

    print(sum_lst[j] - sum_lst[i-1]) # 빼기를 이용해서 정답값 출력 
