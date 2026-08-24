def solution(absolutes, signs):
    
    results = []
    
    for i in range(len(absolutes)):
        if signs[i] == True:
            results.append(absolutes[i])
        elif signs[i] == False:
            results.append(-absolutes[i])
            
    answer = sum(results)
    
    return answer