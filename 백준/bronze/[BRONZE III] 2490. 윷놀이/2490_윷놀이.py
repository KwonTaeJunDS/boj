for i in range(3):
    lst = list(map(int, input().split()))

    if lst.count(0) == 1: # lst의 0의 개수를 세서 그에 따른 도,개,걸,윷,모를 출력
        print('A')
    elif lst.count(0) == 2:
        print('B')
    elif lst.count(0) == 3:
        print('C')
    elif lst.count(1) == 4:
        print('E')
    else:
        print('D')
