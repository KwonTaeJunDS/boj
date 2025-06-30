import sys
num = int(sys.stdin.readline().strip()) 

def check(word): # 그룹 단어 판별 함수수
    visited = set() # 빈 set 자료형을 만들어줌
    pre_chr = '' # 이전 단어 정의 (연속해서 같은 문자가 나올 경우에는 허용하기 위함)
    for chr in word: 
        if chr == pre_chr: # 연속해서 같은 문자가 나오면 pass
            pass
        else: # 연속해서 같은 문자가 아니라면
            if chr in visited: # 만약 set 자료형에 현재 알파벳이 있다면 그룹 단어가 아님
                return False
                break
            else: # set 자료형에 알파벳이 없다면 visited에 chr 추가
                visited.add(chr)
        pre_chr = chr # 이전 단어 갱신
    return True

flag = [] # True, False를 넣어줄 리스트 정의
lst = [] # word를 넣어줄 리스트 정의

for i in range(num):
    word = input()
    lst.append(word)
    flag.append(check(word))

print(flag.count(True)) # True의 갯수를 print해서 그룹 단어 개수 출력
