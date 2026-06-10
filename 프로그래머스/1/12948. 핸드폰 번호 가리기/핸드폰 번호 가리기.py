def solution(phone_number):
    answer = ''
    
    for n in phone_number[:-4]:
        answer += '*'
        
    answer += phone_number[-4:]
    
    return answer