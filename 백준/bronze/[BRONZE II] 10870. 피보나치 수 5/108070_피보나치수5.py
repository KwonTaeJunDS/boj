def Fib(num):
    if num == 0:
        return 0
        
    if num == 1 or num == 2:
        return 1
    else:
        return Fib(num-1) + Fib(num-2)

num = int(input())
print(Fib(num))
