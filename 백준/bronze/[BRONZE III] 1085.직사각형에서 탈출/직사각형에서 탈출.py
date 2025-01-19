x, y, w, h = map(int, input().split()) # 입력 받기

x_zero = x  # 왼쪽 경계까지의 거리 (0에서 시작하니 그대로)
y_zero = y # 아래쪽 경계까지의 거리
x_width = abs(x - w) # 오른쪽 경계까지의 거리
y_height = abs(y - h) # 위쪽 경계까지의 거리

z_num = min(x_zero, y_zero, x_width, y_height) # 최소값이 제일 가까움
print(z_num)
