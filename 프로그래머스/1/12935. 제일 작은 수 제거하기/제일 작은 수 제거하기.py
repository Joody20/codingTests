def solution(arr):
    
    answer = []
    
    if len(arr) == 1:
        answer.append(-1)
    else:
        min_num = min(arr)
        
        for a in arr:
            if a != min_num:
                answer.append(a)
        
    
    return answer
        
    
    