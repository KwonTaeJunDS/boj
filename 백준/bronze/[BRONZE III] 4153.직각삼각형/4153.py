while True:

    a, b, c = list(map(int, input().split()))
    lst = [a,b,c]
    lst.sort()

    if a==b==c==0:
        break

    if lst[0]**2 + lst[1]**2 == lst[2]**2:
        print('right')
    else:
        print('wrong')
