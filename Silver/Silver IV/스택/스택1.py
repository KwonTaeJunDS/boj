import sys

n = int(sys.stdin.readline().strip())


# 기능들 함수로 구현 (굳이 안 그래도 됐을 것 같음)
def push(lst, num):
    lst.append(num)

def pop(lst):
    if len(lst) != 0:
        print(lst.pop())
    else:
        print(-1)

def size(lst):
    print(len(lst))

def empty(lst):
    if len(lst) != 0:
        print(0)
    else:
        print(1)

def top(lst):
    if len(lst) != 0:
        print(lst[-1])
    else:
        print(-1)

lst = []

for i in range(n):
    commend = list(sys.stdin.readline().split())
    if len(commend) == 2:
        order, num = commend[0], commend[1]
    else:
        order = commend[0]

    if order == 'push':
        push(lst, num)
    elif order == 'pop':
        pop(lst)
    elif order == 'size':
        size(lst)
    elif order == 'empty':
        empty(lst)
    elif order == 'top':
        top(lst)
