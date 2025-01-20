 num = int(input())
# h는 호텔의 층수, w는 각 층에 있는 방의 수, n은 몇 번쨰 손님인지
for i in range(num):
    h, w, n = map(int,input().split())
    '''
    층수 계산 
    ex) h=6이고 n=10이라면 10 % 6 = 4 로 4층
    만약 딱 나누어떨어진다면 층수는 h(높이)
    '''
    if n % h==0:
        floor = h
    else:
        floor = n % h
    '''
    손님은 한 층당 한 명씩 배정됨
    h=6이고 n=10이라면 (10 -1) // 6 = 1
    근데 이 식은 0번부터 시작하는 식이라 마지막에 +1을 해줘서 맞춰줌 
    '''
    room_num = (n-1) // h+1
    if len(str(room_num)) == 1: # 만약 방 번호가 두자릿수가 아니면 ex) 1~9 앞에 0을 붙여줌

        room_num = '0' + str(room_num)

    answer = str(floor) + str(room_num)
    print(answer)
