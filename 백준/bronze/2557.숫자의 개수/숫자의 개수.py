a = int(input())
b = int(input())
c = int(input())


answer = str(a*b*c) # count함수 활용을 위해 str로 바꿔줌

for i in range(10):
    num = answer.count(str(i))
    print(num)
