def solution(strings, n):
    answer = {}
    res = []
    
    for word in strings:
        answer[word] = word[n]
        
    sorted_ans = sorted(answer.items(), key=lambda x: (x[1],x[0]))
    
    for word, _ in sorted_ans:
        res.append(word)
    
    
    return res