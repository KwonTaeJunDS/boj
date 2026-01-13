import sys

n = int(sys.stdin.readline().strip())
lst = []
for i in range(n):
    
    commend = sys.stdin.readline().split()
   

    order = commend[0]


    if order == 'push':
        lst.append(int(commend[1]))

    elif order == 'pop':
        if len(lst) != 0:
            value = lst.pop(0)
            print(value)
        else:
            print(-1)
    
    elif order == 'size':
        print(len(lst))
    
    elif order == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)

    elif order == 'front':
        if len(lst) != 0:
            print(lst[0])
        else:
            print(-1)
    
    elif order == 'back':
        if len(lst) != 0:
            print(lst[-1])
        else:
            print(-1)
    else:
        break
