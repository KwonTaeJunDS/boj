import sys

n = int(sys.stdin.readline().strip())
# sys를 사용해 효율적으로 값을 받음
lst = [int(sys.stdin.readline().strip()) for i in range(n)]
# 정렬 
lst.sort()
'''
 리스트 lst에 있는 정수들을 문자열로 바꾸고, 개행 문자 \n으로 연결한 후, 한 번에 출력
'''
# 효율적으로 값을 출력 (print보다 훨씬 빠름) 
sys.stdout.write('\n'.join(map(str, lst))+'\n')
