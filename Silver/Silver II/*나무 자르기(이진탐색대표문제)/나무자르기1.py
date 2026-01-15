import sys

n, m = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))


def bin_search(arr, target, start, end):
    while start <= end:
        
        # 잘라볼 나무 높이 
        mid = (start+end) // 2
        ans = 0

        # 자른 나무 다 더해줌 
        for tree in arr:
            if tree >= mid:
                ans += (tree - mid)

        
        # 자른 나무가 target보다 작다면 end를 줄임 (이래야 target보다 커짐 (빼기니깐))
        if ans < target:
            end = mid - 1
        
        # 자른 나무가 target보다 크다면 start를 키움 (더 빼야 줄어듦)
        elif ans >= target:
            start = mid + 1

    return end



print(bin_search(lst, m, 0, max(lst)))



