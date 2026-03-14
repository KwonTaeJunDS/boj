import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))
lst.sort()

ans = 0

for c in range(n):
    find = lst[c]
    i = 0
    j = n - 1

    while i < j:
        if lst[i] + lst[j] == find:
            if i!=c and j!=c:
                ans +=1
                break
            elif i == c:
                i += 1
            else:
                j -= 1
        elif lst[i] + lst[j] < find:
            i += 1
        else:
            j -= 1
        
print(ans)
