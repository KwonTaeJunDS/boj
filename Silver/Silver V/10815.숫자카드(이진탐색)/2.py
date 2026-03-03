import sys

num1 = int(sys.stdin.readline().strip())
lst1 = list(map(int, sys.stdin.readline().split()))

num2 = int(sys.stdin.readline().strip())
lst2 = list(map(int, sys.stdin.readline().split()))

def bin_search(lst, target):

    start = 0
    end = len(lst) - 1

    while start<=end:
        mid = (start+end) // 2

        if lst[mid] == target:
            return 1
        elif lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

lst1.sort()

for val in lst2:
    ans = bin_search(lst1, val)
    print(ans, end=' ')
