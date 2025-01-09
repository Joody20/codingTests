def solution(jobs):
    
    jobs.sort(key=lambda x:x[0])
    
    current_time = 0
    total_time = 0
    index = 0
    job_count = len(jobs)
    available_jobs = []
    result = 0
    
    while index < job_count or available_jobs:

        while index < job_count and jobs[index][0] <= current_time:
            available_jobs.append(jobs[index])
            index += 1

        if available_jobs:
            available_jobs.sort(key=lambda x: (x[1],x[0]))
            job_start, job_waiting = available_jobs.pop(0)
            current_time += job_waiting
            print(current_time)
            total_time += (current_time - job_start)
        else:
            current_time = jobs[index][0]

    return total_time // job_count       

