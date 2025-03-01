import sys

# 크로아티아 알파벳에 대응할 체크 리스트생성
check_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = str(sys.stdin.readline().strip()) # 단어 입력 받기
# sys 특성상 맨 끝에 개행 문자가 추가되니 strip을 이용해서 없애줌

# 크로아티아 알파벳 개수를 세기 위한 변수 선언 
count = 0 

for i in range(len(word)):
    if word[i:i+3] == 'dz=': # 유일한 세글자인 'dz='를 먼저 확인해줌
        count += 1
    elif word[i:i+2] in check_list: # 이후에 없다면 두글자씩 대응하면서 가줌
        count+=1

print(len(word) - count)
