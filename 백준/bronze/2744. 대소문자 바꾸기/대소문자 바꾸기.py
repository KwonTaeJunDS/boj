word = input() # 입력 받기
answer = ''
for val in word:
    if val.isupper(): # 대문자라면?
        answer += val.lower() # 소문자로 변경
    else:
        answer += val.upper()
print(answer)
