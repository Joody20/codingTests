def solution(array, commands):
    result = []
    
    for i,j,k in commands:
        if i == j:
            split_arr = array[i-1]
            result.append(split_arr)
        else:
            split_arr = array[i-1:j]
            sorted_arr = sorted(split_arr)
            result.append(sorted_arr[k-1])
            
    return result
    