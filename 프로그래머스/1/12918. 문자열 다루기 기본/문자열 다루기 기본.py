def solution(s):
    answer = True
    
    if len(s) not in [4,6]:
        answer = False
    
    if any(c.isalpha() for c in s):
        answer = False
        
    return answer