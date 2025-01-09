def solution(bridge_length, weight, truck_weights):
    second = 0 # 초
    trucks = list(truck_weights) # 올라갈 수 있는 트럭 무게
    bridge = [0] * bridge_length  # 다리의 길이
    s = 0   # 
    
    while (bridge): # bridge의 길이까지
        second += 1  # 초 증가 
        s -= bridge.pop(0)  # 다리 위의 트럭의 총 무게
        print(s)
        if trucks : 
            if s + trucks[0] <= weight:
                s += trucks[0]   # 여유 되면 bridge에 트럭 추가
                bridge.append(trucks.pop(0)) # bridge에 trucks의 첫번쨰 요소 뺀 걸 넣어
                
                print(trucks)
            else:
                bridge.append(0)  # weight 넘어가면 무게 0을 더해
    return second


