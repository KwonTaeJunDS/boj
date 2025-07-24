import sys, math

n = int(sys.stdin.readline().strip())

# 서쪽, 동쪽 사이트 받기 
lst = [list(map(int, sys.stdin.readline().strip().split())) for i in range(n)]



for x,y in lst:
    # math 라이브러리의 comb 함수를 이용해서 간단하게 조합 찾을 수 있음 
    result = math.comb(y, x)
    print(result)
