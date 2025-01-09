def solution(s):
    steps = 0
    total_zero = 0
    
    while len(s) > 1:
        zero = s.count('0')
        total_zero += zero
        
        s = s.replace("0", "") # s의 모든 0을 제외햇어
        s = bin(len(s))[2:]
        
        steps += 1
        
    return [steps, total_zero]
    
