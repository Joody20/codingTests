def solution(s):    
    word = []
    
    for i in s:
        if len(word) == 0:
            word.append(i)
        elif word[-1] == i:
            word.pop()
        else:
            word.append(i)
            
    if len(word) == 0:
        return 1
    else:
        return 0