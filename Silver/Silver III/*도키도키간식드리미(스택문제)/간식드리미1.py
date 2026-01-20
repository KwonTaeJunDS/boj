import sys

n = int(sys.stdin.readline().strip())

lst = list(map(int, sys.stdin.readline().split()))

# 스택 선언
stack = []

# 1번 부터 
target = 1


# 리스트를 다 돔
for val in lst:
    
    # 만약 지금 순서가 target 순서라면 하나 더하기 
    if val == target:
        target += 1

        # 만약 스택에 사람이 있거나 맨 마지막에 들어간 사람이 target이라면 
        while stack and stack[-1] == target:
            stack.pop()
            target += 1
            
    # 지금 순서가 아니라면 스택에 넣어줌
    else:
        stack.append(val)


if stack:
    print('Sad')
else:
    print('Nice')
