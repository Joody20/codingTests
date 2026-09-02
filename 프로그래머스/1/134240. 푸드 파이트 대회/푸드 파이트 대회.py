def solution(food):
    answer = ''
    
    for i in range(1,len(food)):
        
        if food[i] // 2 > 0:
            answer += str(i) * (food[i] // 2)
        else:
            continue
    answer += '0'
    
    
    for j in range(len(food) -1, 0, -1):
        if food[j] // 2 > 0:
            answer += str(j) *(food[j] // 2)
        else:
            continue
            
    return answer