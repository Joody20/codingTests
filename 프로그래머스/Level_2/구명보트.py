def solution(people, limit):
    # 구명보트에는 최대 2명까지만 가능하고
    # 무게 제한 보다 넘으면 안돼 그 구명보트는
    # 사람들을 다 구조를 해야하고 !
    
    # 우리가 리턴해야할 것은 모든 사람을 구출하기 위해 필요한 구명보트의 개수의 최솟값 !!!

    
    count = 0
    n = sorted(people, reverse = True)  # 큰 수 부터 정렬
    
    print(n)
    
    for i in n:
        if i + n[-1] <= limit: 
            n.pop()
        count += 1
    return count
        
            