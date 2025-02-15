import sys

def dp_fib(n):
    dp = [0] * (n+1) # 미리 리스트를 n 크기 만큼 만들어줌
    dp[0], dp[1] = 0, 1 # 첫 번째, 두 번째는 0, 1로 미리 선언
  
    for i in range(2, n+1): # 2부터 n까지 fib수열 만들어줌
        dp[i] = dp[i-2] + dp[i-1]
      
    return dp[n]


num = int(sys.stdin.readline( ))
if num <= 45:
    print(dp_fib(num)) 
