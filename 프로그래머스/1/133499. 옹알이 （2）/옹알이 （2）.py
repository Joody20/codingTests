def solution(babbling):
    answer = 0
    words = ['aya' , 'ye', 'woo', 'ma']
    
    for bab in babbling:
        prev = ""
        i = 0
        success = True
        
        while i < len(bab):
            matched = False
            for word in words:
                if bab[i:i + len(word)] == word and word != prev:
                    prev = word
                    i += len(word)
                    matched = True
                    break
            if not matched:
                success = False
                break
        if success:
            answer += 1
        
    return answer