"""
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20$) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

예제 1
2 4
CAAB
ADCB

출력 1
3

예제 2
3 6
HFDFFB
AJHGDH
DGAGEH

출력 2
6

예제 3
5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH

출력 3
10

"""
from collections import deque
import sys
sys.stdin = open("input.txt","r")

R, C = map(int,input().split()) # 세로, 가로
graph = [list(map(str,input().strip())) for _ in range(R)]

visited = [False] * 26 # 알파벳 개수 26개
max_count = 0


def dfs(x,y,count):
    global max_count
    max_count = max(max_count,count)
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < R and 0<= ny < C:
            char = graph[nx][ny]
            index = ord(char)- ord('A')  # 알파벳을 0부터 25까지의 인덱스로 바꾸기 위해 사용함.
            if not visited[index]:  # 여기서 이제 백트래킹 사용 -> 즉, 이 뜻은 똑같은 알파벳을 방문하지 않았으면, 백트래킹 시도
                visited[index] = True  # 방문처리
                dfs(nx,ny,count + 1)   # 탐색
                visited[index] = False  # 방문해제

            
start_char = graph[0][0]  # 시작점
visited[ord(start_char)- ord('A')] = True  # 시작점을 visited에 넣어줬어야해.. 내가 ord(char) - ord('A) 이 아이디어를 생각 못했음.
# ord(start_char)- ord('A') 이렇게 바꿔주면 알파벳의 방문여부를 쉽게 알 수 있음!!!!!!
dfs(0,0,1)  # dfs에 0,0,횟수 넣어주면 끝.

print(max_count)  # 마지막엔 max_count 리턴


    
    


