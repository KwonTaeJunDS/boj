from itertools import permutations # 모든 경우의 수를 만들기 위한 라이브러리리

n, m = map(int, input().split())
lst = list(map(int, input().split()))

ms = 0
comb_list = list(permutations(lst, 3)) # 3개의 조합으로 모든 경우의 수를 return 해줌 
for i in range(len(comb_list)): # 경우의 수만큼 돌면서
    answer = sum(comb_list[i]) # 해당 경우의 수를 다 더함함
    if answer <= m and answer > ms: # 합이 최대 합보다 같거나 작고, 합이 ms(max sum) 최대 합보다 크면
        ms = answer # 최대합 갱신


print(ms)
