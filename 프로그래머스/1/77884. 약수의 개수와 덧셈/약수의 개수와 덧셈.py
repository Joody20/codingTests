import math

def calculate(n):
    
    results = []
    
    for i in range(1,int(math.sqrt(n)) + 1):
        if n % i == 0:
            results.append(i)
            
            if i != n // i:
                results.append(n//i)
                
    return results
            

def solution(left, right):
    answer = 0
    count = 0
    
    for i in range(left, right + 1):
        count = len(calculate(i))
        
        if count % 2 == 0:
            answer += i
        else:
            answer -= i 
        
    return answer