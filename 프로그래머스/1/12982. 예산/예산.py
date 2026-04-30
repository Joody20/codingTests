from itertools import combinations
def solution(d, budget):
    d.sort()
    
    count = 0
    
    
    for money in d:
        if money <= budget:
            budget -= money
            count += 1
        else:
            break
            
    return count
