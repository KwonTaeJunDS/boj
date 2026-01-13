import sys

n = int(sys.stdin.readline().strip())

lst = [list(sys.stdin.readline().strip()) for i in range(n)]



for i in range(n):
    ans = []
    # flag를 YES로 우선 선언 
    flag = 'YES'
    for j in range(len(lst[i])):
        
        # ( 를 만나면 스택에 넣어줌 
        if lst[i][j] == '(':
            ans.append('(')
        else:
            
            # ) 를 만나면 스택을 pop 해서 () 쌍을 없애줌 
            if len(ans) !=0:
                ans.pop()  

                # 만약 ) 만 있는 상황이라면 이미 조건 탈락. 바로 break
            else:
                flag = 'NO'
                break

    if len(ans) == 0:
        print(flag)
    else:
        flag = 'NO'
        print(flag)
    
