while True:
    a, b = input().split()
    a, b = int(a), int(b)
    if a==0 and b==0:
        break
    if a > b:
        print('Yes')
    else:
        print('No')
