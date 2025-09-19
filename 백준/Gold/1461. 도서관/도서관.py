N,M = map(int,input().split())
books = list(map(int,input().split()))
books.sort() # 오름차순으로 정렬을 먼저 시켜,

result = 0
far_dist = 0

# 음수인 부분은 따로 처리를 먼저 해줘야돼.
if books[0] < 0:
    for i in range(0,N,M): # 처음부터 N까지 M만큼 쩜프!
        if books[i] > 0:  # 양수이면 거르고
            break
        dist = abs(books[i])  # 거리는 절댓값으로 해줘야 음수,양수 중 어떤게 더 먼지 알 수 있음.
        if dist > far_dist: # -> 가장 먼 거리를 far_dist에 넣어줘서 왕복 거리 계산하지 않게! 음수든 양수든 가장 먼 거리를 업데이트 계속 해줌.
            far_dist = dist
        result += dist * 2 # 왕복 거리 계산

# 양수인 부분도 따로 처리
if books[-1] > 0:
    for i in range(N-1,-1,-M): # N부터 끝까지 M만큼 점프!!
        if books[i] < 0: # 양수인 부분에서 음수나오면 거르고
            break
        dist = abs(books[i]) # 거리는 절댓값으로 해줘야 음수,양수 중 어떤게 더 먼지 알 수 있음.
        if dist > far_dist: # -> 가장 먼 거리를 far_dist에 넣어줘서 왕복 거리 계산하지 않게
            far_dist = dist

        result += dist * 2 # 왕복 거리 계산

print(result - far_dist)