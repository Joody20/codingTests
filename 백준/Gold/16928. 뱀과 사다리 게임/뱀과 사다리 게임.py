from collections import deque

N,M = map(int,input().split())
ladders = [list(map(int,input().split())) for _ in range(N)]
snakes = [list(map(int,input().split())) for _ in range(M)]

visited = [0] * 101  #  그냥 칸의 수로 하는거니까 1차원 배열로 해줘야지..

dict_ladders = dict(ladders) # 딕셔너리 형태롤 바꿔줌!
dict_snakes = dict(snakes)


start = 1
end = 100


def bfs(start,end):
    queue = deque()
    queue.append((start,0))  # 현재위치, 주사위 던진 횟수 queue에 넣어주기
    visited[start] = 1


    while queue:
        pos, cnt = queue.popleft()

        if pos == end:
            return cnt # 최소 횟수 반환


        for dice in range(1,7):
            next_pos = pos + dice

            if next_pos > 100:  # next-pos가 100번 칸을 넘어간다면 이동못함.
                continue

            if next_pos in dict_ladders:
                next_pos = dict_ladders[next_pos]

            elif next_pos in dict_snakes:
                next_pos = dict_snakes[next_pos]

            if not visited[next_pos]: # next_pos를 방문하지 않았으면
                visited[next_pos] = 1 # 방문처리 해주고
                queue.append((next_pos, cnt+1))  # queue에 next_pos와 cnt+1해줌.



print(bfs(1,100)) # 시작위치, 끝 위치 넣어주기!