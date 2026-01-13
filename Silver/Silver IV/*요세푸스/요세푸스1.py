import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

# 큐 선언 
q = deque(i for i in range(1, n+1))

# 정답 리스트 선언 
ans = []

for i in range(n):

    # k-1 까지 앞 원소를 빼서 뒤로 넣어줌 
    for j in range(k-1):
        q.append(q.popleft())

    # k 번째는 원소를 빼고 정답에 넣어줌 
    ans.append(q.popleft())


# join 사용에 익숙해지자
print('<'+', '.join(map(str, ans))+'>')
