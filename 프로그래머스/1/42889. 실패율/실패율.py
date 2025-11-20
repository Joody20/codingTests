# from collections import Counter
# def solution(N, stages):
#     stages.sort()
#     users = len(stages)
#     result = dict()
#     ans = []
    
#     for i in range(1,N+1):
#         counts = stages.count(i)
        
#         fail = counts / users
        
#         users = users - counts
        
#         result[i] = fail
        
#     sort_result = sorted(result.items() , key = lambda x : x[1], reverse=True)
    
#     for a,b in sort_result:
#         ans.append(a)
        
#     return ans
        
        
from collections import Counter

def solution(N, stages):
    stage_counts = Counter(stages)
    users = len(stages)
    result = dict()

    for i in range(1, N+1):
        count = stage_counts[i]  # O(1)
        if users == 0:
            result[i] = 0
        else:
            result[i] = count / users

        users -= count

    return sorted(result, key=lambda x: result[x], reverse=True)

    
    