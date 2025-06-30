import sys


# 반복 횟수 
num = int(sys.stdin.readline().strip())

# 그룹 단어 체크 함수 
def is_group_word(word):
    seen = set() # 중복 체크를 위한 set자료형 선언 
    prev = '' # 이전 단어 
    for ch in word: 
        if ch != prev: # 만약 현재 단어가 이전 단어와 다르다면 
            if ch in seen: # 현재 단어가 이미 나왔다면 (seen에 있다면)
                return False 
            seen.add(ch) # 반복문 돌때마다 seen에 단어 추가 
        prev = ch
    return True

# True 개수를 세기 위한 count 
count = 0

for i in range(num): 
    if is_group_word(input().strip()): # 단어 하나씩 들어가야하니 strip 
        count += 1

print(count)
