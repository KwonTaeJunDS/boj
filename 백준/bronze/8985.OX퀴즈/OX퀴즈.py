num = int(input()) # 반복 숫자 입력 받기

for i in range(num):
    lst = list(input()) # OX 입력 받기
    answer = 0 # 정답답
    score = 0 # 더해줄 점수 

    for val in lst:
        if val =='O': # O면 socre에 1을 계속 더하고 그 값을 answer에 더해줌
            score += 1 # O가 연속인 상황을 고려해주기 위해서서
            answer += score
        else: # 만약 X면 score을 초기화
            score = 0
    print(answer)
