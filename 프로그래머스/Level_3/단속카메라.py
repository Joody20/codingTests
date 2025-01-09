def solution(routes):
    routes.sort(key=lambda x:x[1]) # sort함수 안에 key=lambda x:x[1]을 하면 함수를 사용하지 않아도 진입시점과 나간시점을 나눌 수 있음
    
    car_position = -30001 # 차량의 포지션의 최소지점
    camera = 0 # 카메라 개수
    
    for route in routes:
        if car_position < route[0]: # 진입시점이 차량의 포지션보다 크면
            car_position = route[1] # 나간시점이 차량의 포지션이 되고
            camera += 1 # 이 때 카메라 개수를 하나씩 늘려
            
    return camera # 반복문에 나온 후에 그 후에 카메라 개수를 리턴해줌.