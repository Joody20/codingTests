def solution(n, lost, reserve):
    answer = 0
    
    set_lost = set(lost)
    set_reserve = set(reserve)

    common = set_lost & set_reserve  # 공통 집합원소 뽑아내기 -> 이 & 연산은 원소를 뽑는게 아닌 결과는 집합으로 나옴.
    
    
    set_lost = set_lost - common   # 그래서 집합 - 집합을 해줘야 되는거야.
    set_reserve = set_reserve - common
    
    for l in sorted(set_lost):
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