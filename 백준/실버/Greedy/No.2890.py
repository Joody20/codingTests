"""
백준 카약 : https://www.acmicpc.net/problem/2890
상근이는 카약 대회를 개최했다. 대회는 전세계에 생중계되고, 위성이 경기장 전체를 촬영하고 있다. 상근이는 위성 사진을 바탕으로 실시간 순위를 계산하는 프로그램을 만들려고 한다.

위성 사진은 R행 C열이다. 모든 줄의 첫 번째 글자는 'S'이고 출발선을 의미한다. 또, 마지막 글자는 'F'이고 이것은 결승선을 의미한다. 대회에 참가한 팀은 총 9팀이고, 각 팀은 1부터 9까지 번호가 매겨져 있다. 카약은 항상 열에 대해 연속하는 세 칸을 차지하며, 카약 번호로 표시한다. 마지막으로 물은 '.'로 나타나 있다.

팀의 순위는 결승선으로부터 떨어진 거리로 측정한다. 가까울수록 순위가 높다. 만약, 두 팀이 결승선과 떨어진 거리가 같다면, 같은 등수이다.

첫째 줄에 R과 C가 주어진다. 다음 R개 줄에는 '.', 'S', 'F', '1'~'9'로 이루어진 위성 지도가 주어진다. 한 줄에는 최대 한 개의 카약만 있고, 위성 사진에 있는 카약은 항상 9개이다. (10 ≤ R, C ≤ 50)

출력
출력은 총 9줄을 해야 한다. i번째 줄에는 i번 팀의 등수를 출력한다. (i=1~9)


예제 1
10 10
S.....111F
S....222.F
S...333..F
S..444...F
S.555....F
S666.....F
S.777....F
S..888...F
S...999..F
S........F

출력 1
1
2
3
4
5
6
5
4
3

예제 2
10 15
S..........222F
S.....111.....F
S...333.......F
S...555.......F
S.......444...F
S.............F
S......777....F
S..888........F
S........999..F
S...666.......F

출력 2
5
1
6
3
6
6
4
7
2

"""


import sys
sys.stdin = open("input.txt","r")

row , col = map(int,input().split())
race = [input() for _ in range(row)]
number = ['1','2','3','4','5','6','7','8','9']

num_idx = 0
f_idx = 0
result = []
for i in range(row):
    for n in number: 
        if n in race[i]:  # n이 race[i]에 있으면
            num_idx = race[i].rfind(n)  # rfind 써주면 그 숫자의 마지막 인덱스 번호를 리턴해줌.
            f_idx = race[i].find('F')  # F 결승점 인덱스 번호 구해주고
            result.append((int(race[i][num_idx]), race[i][num_idx+1:f_idx].count('.')) )  # 일단, 카약의 번호랑, 나는 인덱스로 슬라이싱 해서 그 사이의 .의 개수를 세어줬어. 그걸 result 배열에 넣어줬고!


value = [x[1] for x in result]   # .의 개수만 빼내서
sorting_value = sorted(set(value))  # 이게 .의 개수센거 sorting한거야. set을 꼭 붙여줘야 되는데?
ranking = {value: rank + 1 for rank, value in enumerate(sorting_value)} # 이게 이제 .의 개수센거대로 순위 매겨준거야.
ranked = [(x[0],x[1],ranking[x[1]]) for x in result]  # 여기에 이제 원래 카약의 번호,.의 개수, 순위 매긴거 배열로 정리
sorted_rank = sorted(ranked,key=lambda x:x[0])  # 이제 카약의 번호 대로 sorting하고

for s in sorted_rank: # 순위 매긴거 출력
    print(s[2])



