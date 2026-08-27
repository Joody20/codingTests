import math
def calculate_div(n):
    result = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.append(i)
            
            if i != n // i:
                result.append(n//i)
                
    return result
        
    
def solution(n, m):
    answer = []
    max_a = 0
    min_b = 0
    
    res_n = calculate_div(n)
    res_m = calculate_div(m)
    
    for r in res_n:
        if r in res_m:
            if max_a < r:
                max_a = r
                
    answer.append(max_a)
    
    min_b = n * m // math.gcd(n,m)
    answer.append(min_b)
            
    
    
    return answer