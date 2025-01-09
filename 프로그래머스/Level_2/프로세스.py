def solution(priorities, location):
    priorities = [[x,i] for i,x in enumerate(priorities) ]
    
    i=1
    
    while priorities:
        now = priorities[0]
        
        priorities.remove(now)
        if all(now[0] >= x[0] for x in priorities) and now[1] == location:
            return i
        elif all(now[0] >= x[0] for x in priorities):
            i += 1
        else:
            priorities.append(now)
        
        