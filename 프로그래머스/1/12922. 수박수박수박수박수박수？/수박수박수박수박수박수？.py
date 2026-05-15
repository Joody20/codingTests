def solution(n):
    answer = ''
    word = '수박'

    
    for _ in range(n):
        answer += word
        
    answer = answer[:n]
    
        
    return answer