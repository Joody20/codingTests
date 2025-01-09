def solution(n):
    #자연수 n을 연속한 자연수들로 표현하는 방법이 여러개지 
    # 일단 n은 0보다 큰 수여야 돼 그리고 덧셈만 가능하고
    # 연속적이어야돼.
    # i는 무조건 하나씩 증가돼서 15가 되어야 되는거야
    count = 0
    for i in range(1, n+1):
        result = 0
        while(result < n):
            result += i
            i += 1
        if(result == n):
            count += 1
    return count