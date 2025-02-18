num = int(input())

for i in range(num):
    count = 0
    lst = list(map(int, input().split()))
    avg = sum(lst[1:]) / lst[0] # lst의 0번째 인덱스는 과목 수이므로 인덱스 1부터
    
    for j in range(lst[0]):
        if lst[j+1] > avg:
            count +=1
    print(f'{count / lst[0] * 100:.3f}%')
