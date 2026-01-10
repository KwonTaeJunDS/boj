import sys

n, m = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))


length = len(lst)

def black(lst):
    ans = 0
    # 정렬을 통해 연산 효율성 높임 
    lst.sort()

    # 완전 탐색해야 하니 3중 for문 
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                flag = (lst[i] + lst[j] + lst[k])

                # 세 합이 m보다 크다면 탐색 중지 
                if flag > m:
                    break
                
                # max를 통해 갱신 (연산 효율성)
                ans = max(ans, flag)


        
    return ans


print(black(lst))

