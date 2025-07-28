import sys

n = int(sys.stdin.readline().strip())

# 팩토리얼 함수 구현 
def fact(n):
    if n > 1:
        return n * fact(n-1)
    else:
        return 1
    
# 0을 찾아내기 위해 문자형으로 변환     
answer = str(fact(n))


c = 0

# 뒤에서 부터 확인하기 위해 reversed 사용 
for ch in reversed(answer):
    if ch == '0':
        c += 1
    else:
        break

print(c)
