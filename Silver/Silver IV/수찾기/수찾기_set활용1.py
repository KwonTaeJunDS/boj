import sys

n = int(sys.stdin.readline().strip())
lst = set(map(int, sys.stdin.readline().split()))


k = int(sys.stdin.readline().strip())
new_lst = list(map(int, sys.stdin.readline().split()))



for target in new_lst:
    if target in lst:
        print(1)
    else:
        print(0)
