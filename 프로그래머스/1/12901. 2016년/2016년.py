def solution(a, b):
    answer = ''
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    weeks = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    day = sum(days[:a-1]) + (b-1)
    
    answer = weeks[day % 7]
        
        
        
    return answer