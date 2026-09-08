from collections import Counter
def solution(participant, completion):
    count = Counter(completion)
    
    result = []
    
    for par in participant:
        if count[par] > 0:
            count[par] -= 1
        else:
            result.append(par)
    
    result = "".join(result)

    return result