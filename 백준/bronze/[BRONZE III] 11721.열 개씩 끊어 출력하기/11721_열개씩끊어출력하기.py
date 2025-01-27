lst = input() # 문자열 받고
lst = list(lst)

num = 0 # list 인덱스 갱신을 위한 num 변수 선언
for i in range(len(lst)//10 + 1): # 이중 for 문을 이용해서 진행
    for j in range(10):
        num += 1
        if num > len(lst): # num이 lst의 길이를 넘어갈 경우 for문 탈출
            break
        else:
            print(lst[num-1], end='')
    print() # 10 문자마다 개행
