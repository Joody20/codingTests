"""
백준 단지번호(실버 1) : https://www.acmicpc.net/problem/2667

<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

첫 번째 줄에는 총 단지수를 출력하시오. 그리고 "각 단지내 집의 수" 를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

예제:
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

"""

import sys
sys.stdin = open("input.txt","r")

N = int(input())

graph = [list(map(int,input())) for _ in range(N)]

result = 0
home_counts = [] # 각 집 단지의 집의 개수를 넣을

## 그룹 내에 1의 개수를 구할려면 !dfs 함수 안에서 해야돼 그니까 그 함수에 count + 1씩 해주는거야

def dfs(x,y):
    if x <= -1 or x >= N or y<= -1 or y >= N:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0

        count = 1

        count += dfs(x-1, y) 
        count += dfs(x, y-1)
        count += dfs(x+1, y)
        count += dfs(x,y+1)

        return count
    
    return 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:  # 1이면
            home_count = dfs(i,j) # dfs 함수에 전달을 해 그 위치를
            if home_count > 0: # 0보다 크면
                home_counts.append(home_count) # 그걸 이제 배열 안에 넣고
                result += 1 # true인 거니까 result += 1씩 해주고

print(result)
print("\n".join(map(str,sorted(home_counts)))) # 오름차순으로 정렬해서 리턴해줌.
