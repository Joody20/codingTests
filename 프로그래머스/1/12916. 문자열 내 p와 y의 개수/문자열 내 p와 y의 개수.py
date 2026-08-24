def solution(s):
    answer = True
    
    p_count = 0 
    y_count = 0
    

    for ss in s:
        if ss == 'p' or ss == 'P':
            p_count += 1
        elif ss == 'y' or ss == 'Y':
            y_count += 1
    

    if p_count == y_count or p_count == 0 and y_count == 0:
        answer = True
    else:
        answer = False
        
    return answer