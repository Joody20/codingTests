def solution(n, lost, reserve):
    # 여벌 체육복이 있는 학생이 체육복을 도난당한 경우에는 빌려줄 수 없어 이걸 처리해줘야돼.
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    
    for r in sorted(reserve_set):
        if (r - 1) in lost_set:
            lost_set.remove(r-1)
        elif (r + 1) in lost_set:
            lost_set.remove(r+1)
            
    return n - len(lost_set)
            
