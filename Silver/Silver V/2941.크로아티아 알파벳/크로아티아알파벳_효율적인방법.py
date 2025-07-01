# 크로아티아 알파벳 
check = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


import sys

# 문자 입력 받기
word = sys.stdin.readline().strip()

# 크로아티아를 순회하면서 
for ch in check: # 입력받은 문자열에 크로아티아 알파벳이 있다면 '*' 로 치환
    word = word.replace(ch, '*')

print(len(word))
