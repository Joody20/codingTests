def solution(s):
    answer = ''
    mid = 0
    
    if len(s) % 2 == 0: # 짝수인 경우
        mid = len(s) // 2
        answer += s[mid - 1]
        answer += s[mid]
        
    else:
        mid = len(s) // 2
        answer += s[mid]
        
    return answer