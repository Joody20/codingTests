import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0 # 횟수
    
    
    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        
        if first >= K:
            return count

        second = heapq.heappop(scoville)
        
        new_sco = first + (second * 2)
        heapq.heappush(scoville , new_sco)
        
        count += 1
        
    return count if scoville[0] >= K else -1