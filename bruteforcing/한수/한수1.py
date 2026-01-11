import sys

n = int(sys.stdin.readline())

cnt = 0
for i in range(1, n+1):
    # 100 이하는 무조건 한수
    if i < 100:
        cnt += 1

    # 100 이상부터 즉 세 자릿수부터 직접 비교 
    else:
        lst = list(map(int, str(i)))
        if lst[0] - lst[1] == lst[1] - lst[2]:
            cnt += 1



print(cnt)
