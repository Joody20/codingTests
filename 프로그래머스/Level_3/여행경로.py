def solution(tickets):
    # tickets의 각 행 [a,b]는 a 공항에서 b공항으로 가는 항공권이 존재
    # if 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return
    
    ticket = {}  # 비행기 항공권의 딕셔너리
    
    for start, end in tickets:
        if start not in ticket:
            ticket[start] = []
        ticket[start].append(end)
        
    for key in ticket:
        ticket[key].sort(reverse=True) # 알파벳 역순으로 목적지 목록을 정렬 
        print(ticket[key])
                    
            
    departure = ["ICN"] 
    route = []
    
    while departure:
        current = departure[-1]# 끝에 있는 출발지를 현재 방문한 곳
        if current in ticket and ticket[current]: # 현재 목적지가 남아있으면 
            departure.append(ticket[current].pop()) # departure에 현재 공항을 pop 한 후에 append
        else: # 더이상 목적지가 없다면 route에 현재 공항 추가
            route.append(departure.pop())
            
    return route[::-1] # 경로를 역순으로 구축하기에 마지막을 -1로 리턴해주는거임.