def solution(s):
    answer = []
    
    # 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로
    
    string = s.split(" ")
    
    for ss in string:
        word = ''
        for i in range(len(ss)):
            if i == 0:
                word += ss[i].upper()
            elif i % 2 == 0:
                word += ss[i].upper()
            else:
                word += ss[i].lower()
        
        answer.append(word)
    
    
    result = " ".join(answer)
    
    return result