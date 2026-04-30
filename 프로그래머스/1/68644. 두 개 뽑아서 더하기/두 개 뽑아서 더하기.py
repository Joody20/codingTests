from itertools import permutations
def solution(numbers):
    result = set()
    
    for res in permutations(numbers, 2):
        result.add(sum(res))
    
    return sorted(list(result))