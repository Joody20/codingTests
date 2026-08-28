def solution(s):
    answer = []
    dict_s = {}
    
    
    for i, char_idx in enumerate(s):
        if char_idx in dict_s:
            answer.append(i - dict_s[char_idx])
            
        else:
            answer.append(-1)
        
        dict_s[char_idx] = i
    
    
        
    return answer