import sys

n = int(sys.stdin.readline().strip())

a = list(map(int, sys.stdin.readline().strip().split()))
# 비교 대상 리스트 정렬 
a.sort()

n = int(sys.stdin.readline().strip())
b = list(map(int, sys.stdin.readline().strip().split()))

lst = []

# 이진 탐색 알고리즘 정의 
def binary(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == num:
            return 1
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return 0 

for num in b:
    lst.append(binary(a, num))

print(*lst)
