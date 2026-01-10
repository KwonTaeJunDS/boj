import sys 

n = int(sys.stdin.readline())



ans = 0

# 1부터 n까지 다 돌기
for i in range(1, n):
    # 분해합 찾기
    flag = i + sum(map(int, str(i)))
    if flag == n:
        ans = i
    
        break
    else:
        ans = 0

print(ans)

    

