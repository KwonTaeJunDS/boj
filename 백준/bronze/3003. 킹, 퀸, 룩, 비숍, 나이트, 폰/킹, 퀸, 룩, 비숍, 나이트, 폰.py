target = [1, 1, 2, 2, 2, 8] # 체스 개수
lst = list(map(int, input().split())) # 갖고 있는 체스 개수 입력 받기
# zip을 이용해서 for문으로 돌면서 빼기 진행행
answer = [print(target - lst, end=' ') for target, lst in zip(target,lst)]
