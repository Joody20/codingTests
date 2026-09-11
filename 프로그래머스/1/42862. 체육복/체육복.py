def solution(n, lost, reserve):
    중복없는lost = set(lost) - set(reserve)
    중복없는reverse = set(reserve) - set(lost)
    
    for r in sorted(중복없는reverse):
        if (r-1) in 중복없는lost:
            중복없는lost.remove(r-1)
        elif (r+1) in 중복없는lost:
            중복없는lost.remove(r+1)
    
    
    return n - len(중복없는lost)
            
