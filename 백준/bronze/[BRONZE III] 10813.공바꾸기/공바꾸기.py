n, m = map(int, input().split())

basket = [i for i in range(1,n+1)] # 순서대로 바구니 리스트 생성성

for i in range(m): # 교환환
    a, b = map(int, input().split())
    a, b = a-1, b-1 # 리스트 인덱스에 맞추기 위해서 - 1
    new = basket[a]
    basket[a] = basket[b]
    basket[b] = new

print(*basket)
