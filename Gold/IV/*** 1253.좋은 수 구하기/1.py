import sys

num = int(sys.stdin.readline().strip())

lst = list(map(int, sys.stdin.readline().split()))

lst.sort() # 정렬 

ans = 0

for c in range(num):
    # 현재 찾아야할 값 
    find = lst[c]
    i = 0
    j = num - 1

    while i < j :
        # 만약 좋은 수 라면 
        if lst[i] + lst[j] == find:
            
            # 그 값이 본인 숫자 c가 아니라면 좋은 수 맞음 
            if i != c and j != c:
                ans +=1 
                break
            # 그게 아니라면 i하고 j 값 변경 (좁혀가는 방향으로)
            elif i==c:
                i += 1
            elif j==c:
                j -= 1
        
        # 만약 찾아야할 값보다 작다면 i하고 j 변경 
        elif lst[i] + lst[j] < find:
            i += 1
        else:
            j -= 1


print(ans)

        
        


