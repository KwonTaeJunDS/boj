import sys

num = int(sys.stdin.readline().strip())

ans = 0

while num >= 0:
    if num % 5 == 0:
        ans += num // 5
        num = 0
        break
    else:
        num -= 3
        ans += 1


        
if num != 0:
    ans= - 1
    
print(ans)
