import sys

n = int(sys.stdin.readline().strip())

cnt = 0


while n >= 0:
    # n이 만약 5로 나누어 떨어지면 반복문 탈출 
    if n % 5 == 0:
        cnt += n // 5
        n = 0
        break
    # 아니라면 3을 빼면서 cnt 증가 
    else:
        n -= 3
        cnt += 1

# 만약 나누어 떨어지지 않는다면 -1 출력 
if n != 0:
    print(-1)
else:
    print(cnt)
