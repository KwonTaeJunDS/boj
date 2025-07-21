import sys

x = int(sys.stdin.readline().strip())


hap, line = 0, 0

# x의 n번째 대각선 찾기
while hap < x:
    line += 1
    hap += line

# n번째 대각선 내 n번째 위치 찾기 
iline = x - (hap - line)

# 홀수번째 대각선이면 ↗
if line % 2 != 0:
    up = line - iline + 1
    down = iline
else: # 짝수번째 대각선이면 ↙
    up = iline
    down = line - iline + 1

print(f'{up}/{down}')
