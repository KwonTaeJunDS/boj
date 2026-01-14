import sys

n = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

# 타겟은 그대로 있는지 없는지 출력해야 하니 정렬하지 않음
k = int(sys.stdin.readline().strip())
target = list(map(int, sys.stdin.readline().split()))


# 이진 탐색 함수 선언 
def bin_search(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if arr[mid] == target:
            return 1
        
        elif arr[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1
    return 0

for val in target:
    print(bin_search(lst, val, 0, n-1))
