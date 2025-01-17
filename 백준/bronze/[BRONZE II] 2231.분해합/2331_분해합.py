num = int(input())
answer = 0


for i in range(num): # 입력받은 숫자까지 for문으로 반복복
    new_sum = i + sum([int(j) for j in str(i)]) # i와 그에 해당하는 i의 자릿수를 다 더한것을 합함
    if new_sum == num: # 만약 그 답이 입력받은 숫자와 같다면 생성자임

        answer = i
        break
    else: # 만약 생성자가 없다면 0 return
        answer = 0
print(answer)
