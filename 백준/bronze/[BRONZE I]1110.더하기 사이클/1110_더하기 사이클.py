num = input() 

count = 0
if len(num) == 1: # 입력받은 수가 1자리수라면 앞에 0 붙여줌줌
    num = '0' + num

answer = num # 그 값을 정답으로 정의의


while True: # 무한 반복복
    if num == '00': # 만약 입력값이 0이라면 1 출력하고 탈출출
        print(1)
        break
    else:   # 문제에서 주어진 규칙에 따라 계산
        new_num = str(int(num[0]) + int(num[1]))
        count += 1
        new_num = str(num[1]) + str(new_num[-1]) 
        if new_num == answer: # 계산해서 나온 새로운 숫자가 answer과 같다면 탈출 
            print(count)
            break
        num = new_num
    
