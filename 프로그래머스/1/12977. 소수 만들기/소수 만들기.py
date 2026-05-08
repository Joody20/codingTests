from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    
    result = []
    
    for num in combinations(nums, 3):
        total = sum(num)
        
        result.append(is_prime(total))
        
    
    return result.count(True)
    
        
        
        
            
        
    
    