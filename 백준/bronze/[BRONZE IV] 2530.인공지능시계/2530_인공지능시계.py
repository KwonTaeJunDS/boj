h, m, s = map(int, input().split())
num = int(input())

total_s = h * 3600 + m * 60 + s + num # 일단 초로 전부 변환

h = (total_s // 3600) % 24 # 시간은 3600초로 나누고 이를 24로 나눠서 나머지지
m = (total_s % 3600) // 60 # 초를 3600초로 나눠서 나머지를 60으로 나누기
s = total_s % 60 # 초를 60으로 나눠서 나머지 

print(h, m, s)
