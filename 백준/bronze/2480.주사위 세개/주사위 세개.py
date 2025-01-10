# 내 코드
a, b, c = map(int,input().split())

if a == b == c:
    print(10000 + a*1000)
elif a==b or b==c or a==c:
    if a==b:
        print(1000+a*100)
    elif b==c:
        print(1000+b*100)
    else:
        print(1000+a*100)
else:
    num = max(a,b,c)
    print(num*100)
  
'''
--------------------------
'''

# GPT 코드
a, b, c = map(int, input().split())
numbers = [a, b, c]

if len(set(numbers)) == 1:  # 모두 같은 경우
    print(10000 + a * 1000)
elif len(set(numbers)) == 2:  # 두 개가 같은 경우
    for num in numbers: # 요기 코드가 진짜 좋은듯 count를 이용해서 2개가 중복인 num을 찾아낸다다
        if numbers.count(num) == 2:
            print(1000 + num * 100)
            break
else:  # 모두 다른 경우
    print(max(numbers) * 100)
