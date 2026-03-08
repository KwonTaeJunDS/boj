import sys

num = int(sys.stdin.readline().strip())

lst = list(map(int, sys.stdin.readline().split()))

target = 1 # 간식 주는 순서 

stack = []

for val in lst:
    if val == target: # 만약 학생이 지금 순서라면 다음 순서로
        target += 1

        while stack and stack[-1] == target: # 스택에 쌓인 다음 순서가 있다면 확인 
            
            stack.pop()
            target += 1

    else: # 현재 순서가 아니라면 스택에 학생을 쌓아둠
        stack.append(val)

if stack: # 스택에 학생이 있다면 실패
    print('Sad')
else: # 스택이 비어있다면 성공 (잘 나눠줌)
    print('Nice')
