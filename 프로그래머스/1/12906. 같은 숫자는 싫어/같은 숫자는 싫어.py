def solution(arr):
    result = [arr[0]]
    
    for a in arr:
        if result[-1] == a:
            continue
        else:
            result.append(a)
            
    
    
    return result