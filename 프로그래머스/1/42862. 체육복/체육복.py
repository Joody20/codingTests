def solution(n, lost, reserve):
    answer = 0
    
    set_lost = set(lost)
    set_reserve = set(reserve)

    common = set_lost & set_reserve
    
    set_lost = set_lost - common
    set_reserve = set_reserve - common
    
    for l in set_lost.copy():
        if l-1 in set_reserve:
            set_lost.remove(l)
            set_reserve.remove(l-1)
        elif l+1 in set_reserve:
            set_lost.remove(l)
            set_reserve.remove(l+1)
        else:
            continue
    
    answer = n - len(set_lost)
    return answer