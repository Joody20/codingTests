def solution(progresses, speeds):
    answer = []
    task = []
    count = 0
    maxDays = 0
    
    for i in range(len(speeds)):
        남은진도 = 100 - progresses[i]
        작업기간 = (남은진도 + speeds[i] - 1) // speeds[i]
        
        task.append(작업기간)
    
    for t in task:
        if t > maxDays:
            if count > 0:
                answer.append(count)
            count = 1
            maxDays = t
        else:
            count += 1
        
    answer.append(count)
        
    return answer