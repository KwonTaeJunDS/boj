def primenumber(x):
    if x == 1: # 1은 소수에서 제외외
        return False
    for i in range(2, x): # 만약 나눠지면 소수가 아님 False return
        if x % i == 0:
            return False

    return True

num = int(input())

lst = list(map(int, input().split()))
answer = []
for val in lst: # 입력 받은 숫자들을 돌면서 판정
    if primenumber(val):
        answer.append(val) #answer에 소수들만 append

print(len(answer)) # 소수 개수 출력
