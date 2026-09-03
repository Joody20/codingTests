def solution(k, score):
    answer = []
    awards = [] # k개의 원소만 들어갈 수 있고, 정렬이 안되도돼. 최소값만 던져주면 되는데..
    
    for s in score:
        if len(awards) < k: # 명예의 전당 자리가 k보다 작으면
            awards.append(s)
        else: # k보다 커지면
            if min(awards) <= s:
                awards.remove(min(awards))
                awards.append(s) 
        answer.append(min(awards))
        
    return answer