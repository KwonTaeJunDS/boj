s = list(input().split()) # 리스트로 받아 공백을 기준으로 전부 분리

for val in s:
    if val == ' ': # 리스트를 돌면서 공백이면 제거
        s.remove(val)

print(len(s))
