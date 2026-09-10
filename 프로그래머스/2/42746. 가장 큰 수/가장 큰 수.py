from itertools import combinations
def solution(numbers):
    numlist = list(map(str, numbers))
    
    numlist.sort(key= lambda x : x*3, reverse = True)
    answer = "".join(numlist)
    
    if answer[0] == '0':
        return "0"
    return answer
    
    