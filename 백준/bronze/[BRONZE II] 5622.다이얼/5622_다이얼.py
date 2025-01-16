phone = {2:'ABC', 3:'DEF', 4:'GHI', 5:'JKL', 6:'MNO', 7:'PQRS', 8:'TUV', 9:'WXYZ'}

string_num = list(input())
answer = 0

for val in string_num:
    for k, v in phone.items():  # 딕셔너리를 이용해서 찾아냄냄
    
        if val in v:
            answer += (k+1) # 숫자 1을 누를때 2초가 걸리니 각 숫자마다 1씩 더해줌줌

print(answer)
