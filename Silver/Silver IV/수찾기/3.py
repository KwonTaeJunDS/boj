import sys

num_1 = int(sys.stdin.readline().strip())
lst_1 = list(map(int, sys.stdin.readline().split()))

num_2 = int(sys.stdin.readline().strip())
lst_2 = list(map(int, sys.stdin.readline().split()))

lst_1.sort()

def bin(lst, target):
    start = 0
    end = len(lst)- 1

    while start <= end:
        mid = (start+end)//2
        
        if lst[mid] == target:
            return 1
        elif lst[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return 0




for val in lst_2:
    ans = bin(lst_1, val)
    print(ans)
