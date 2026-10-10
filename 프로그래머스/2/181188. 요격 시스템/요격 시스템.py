def solution(targets):
    answer = 0
    targets.sort(key=lambda x:(x[1],x[0]))
    
    cnt = 0
    start = 0
    end = 0
    
    for s,e in targets:
        
        # 끝나는 지점이 s,e 구간안에 있으면 cnt += 1이야.
        if s >= end:
            start = s
            end = e
            cnt += 1
        
    
    return cnt