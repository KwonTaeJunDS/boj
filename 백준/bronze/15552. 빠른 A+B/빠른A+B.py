import sys

while True:
    # sys.stdin.readline은 맨 끝의 개행문까지 같이 입력받기 때문에 .rstrip()을 추가
    num = sys.stdin.readline().rstrip() # input()과 같은 역할을 하지만 빠른 입력 지원 
    if num == '': # 입력을 받지 않으면 종료
        break
    else: 
        for i in range(int(num)):
            a, b = map(int, sys.stdin.readline().rstrip().split())
            print(a+b)
