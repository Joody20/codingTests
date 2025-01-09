def solution(operations):
    queue = []
    
    for operation in operations:
        if operation[0] == 'I':
            _, value = operation.split()
            value = int(value)
            queue.append(value)
            
        elif operation[0] == 'D':
            _, value = operation.split()
            if not queue:
                continue
                
            if value == '1':
                max_value = max(queue)
                queue.remove(max_value)
                
            elif value == '-1':
                min_value = min(queue)
                queue.remove(min_value)
    if not queue:
        return [0,0]
    else:
        return[max(queue),min(queue)]