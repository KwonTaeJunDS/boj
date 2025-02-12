n, m = map(int, input().split())
lst = [i for i in range(1, n+1)] # 초기 바구니 정의의

for i in range(m):
    a, b = map(int, input().split())
    if a == 1: # 만약 a가 1이면 역 슬라이싱 특성상 인덱스를 부여하면 끝까지 안감
        newlst = lst[b-1::-1]
        lst[a-1:b] = newlst # 초기 바구니 순서 변경경
    else:
        newlst = lst[b-1:a-2:-1]
        
        lst[a-1:b] = newlst
    

print(*lst)
