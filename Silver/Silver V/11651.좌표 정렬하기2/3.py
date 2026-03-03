import sys

n = int(sys.stdin.readline().strip())

cor = []
for i in range(n):
    cor.append(list(map(int, sys.stdin.readline().split())))


cor = sorted(cor, key=lambda x: (x[1], x[0]))
# print(cor)

for lst in cor:
    print(*lst)
