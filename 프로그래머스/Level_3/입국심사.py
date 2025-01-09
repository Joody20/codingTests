def solution(n, times):
    left = 1  # 최소 1분은 기다릴 수도 있는 사람
    right = max(times) * n # 최대 times에서 인원수만큼 기다릴 수도 있는 사람
    answer = right
    
    while left <= right:
        mid = (left + right) // 2 # 중간시간에서 처리할 수 있는 인원 체크하기 위함임.
        people  = 0 # 사람들
    
        for time in times:
            people += mid // time # 중간시간안에 모든 people이 들어갈 수 있는지
            if people >= n: # 들어갈 수 있는 사람이 n보다 크면 break
                break
                
                
        if people >= n: # n보다 people이 크면 
            answer = mid
            right = mid -1
        else: # people이랑 n이랑 같으면 mid + 1
            left = mid + 1
            print(left)

    return answer