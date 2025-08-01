import sys

n = int(sys.stdin.readline().strip())

# 빈 set 선언 
S = set()

for _ in range(n):
    # 매 반복마다 명령고 숫자 받음 
    command = sys.stdin.readline().strip().split()

    # 문제에서 요구하는대로 구현 
    # 받은 숫자는 정수형이 아니니 항상 int로 바꿔줌 
    if command[0] == 'add': S.add(int(command[1]))
    elif command[0] == 'remove': S.discard(int(command[1]))
    elif command[0] == 'check': sys.stdout.write('1\n' if int(command[1]) in S else '0\n')
    elif command[0] == 'toggle': 
       if int(command[1]) in S:
         S.discard(int(command[1]))
       else:
         S.add(int(command[1]))

    elif command[0] == 'all': S=set(range(1,21))
    elif command[0] == 'empty': S = set()
