import sys

n = int(sys.stdin.readline().strip())
# sys를 사용해 효율적으로 값을 받음
lst = [int(sys.stdin.readline().strip()) for i in range(n)]
# 정렬 
lst.sort()
# 효율적으로 값을 출력 (print보다 훨씬 빠름) 
sys.stdout.write('\n'.join(map(str, lst))+'\n')
