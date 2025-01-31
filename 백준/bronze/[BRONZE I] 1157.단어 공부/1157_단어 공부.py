word = input() # 단어 입력 받고
word = word.lower() # 전부 소문자로 변경경
lst = dict() # 단어 중복 개수를 알기 위한 dict 선언언
set_word = set(list(word)) # set을 이용해 중복을 다 없애고

for val in set_word: # count를 통해서 중복 개수를 세어줌줌
    lst[val] = word.count(val)

# value 즉 중복 count 수를 이용해 내림차순 정렬렬
lst = sorted(lst.items(), key=lambda x:x[1], reverse=True)

num = len(lst) # 'aa' 라는 문자열이 들어왔을때를 대비하여 lst 길이 선언
if num == 1: # 만약 한글자라면 그냥 바로 대문자로 바꾸고 print
    print(lst[0][0].upper())
else:
    if lst[0][1] == lst[1][1]: # 많이 나온 알파벳 개수가 같다면 '?' print
        print('?')
    else:
        print(lst[0][0].upper())
