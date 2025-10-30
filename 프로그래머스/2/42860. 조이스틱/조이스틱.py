def solution(name):
    answer = 0
    name_len = len(name)
    minCursor = name_len - 1
    
    # 알파벳 최소 움직임
    for i, n in enumerate(name):
        answer += min(ord(n) - ord('A'), ord('Z') - ord(n) + 1)
        
    
        # 커서 움직임 최소 횟수 
        nextCursor = i + 1
        while (nextCursor < name_len and name[nextCursor] == 'A'):
            nextCursor += 1

        distance = min(i, name_len - nextCursor)
        minCursor = min(minCursor , i + (name_len - nextCursor) + distance)
        
    answer += minCursor
    
    return answer

    