import sys

n, hap = map(int, sys.stdin.readline().strip().split())

lst = list(map(int, sys.stdin.readline().strip().split()))
lst.sort()

ans = 0

# for문을 통해서 모든 리스트 순회 
for i in range(len(lst)- 2):
    for j in range(i+1, len(lst)-1):
        for k in range(j+1, len(lst)):
            # 순회하면서 처음 3개의 숫자 더함
            hh = (lst[i] + lst[j] + lst[k])
            # 목표보다 작다면 ans에 넣어줌
            if  hh <= hap:
                ans = max(hh, ans)
            # 목표를 넘으면 멈춤     
            else:
                break

print(ans)
