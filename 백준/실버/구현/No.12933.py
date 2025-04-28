"""
백준 실버 2 오리 : https://www.acmicpc.net/problem/12933

https://velog.io/@gilyeon00/%EB%B0%B1%EC%A4%80-12933%EB%B2%88-%EC%98%A4%EB%A6%AC-python-%EC%8B%A4%EB%B2%843
-> 이 블로그 참고

오리의 울음 소리는 "quack"이다. 올바른 오리의 울음 소리는 울음 소리를 한 번 또는 그 이상 연속해서 내는 것이다. 예를 들어, "quack", "quackquackquackquack", "quackquack"는 올바른 오리의 울음 소리이다.

영선이의 방에는 오리가 있는데, 문제를 너무 열심히 풀다가 몇 마리의 오리가 있는지 까먹었다.

갑자기 영선이의 방에 있는 오리가 울기 시작했고, 이 울음소리는 섞이기 시작했다. 영선이는 일단 울음소리를 녹음했고, 나중에 들어보면서 총 몇 마리의 오리가 있는지 구해보려고 한다.

녹음한 소리는 문자열로 나타낼 수 있는데, 한 문자는 한 오리가 낸 소리이다. 오리의 울음 소리는 연속될 필요는 없지만, 순서는 "quack"이어야 한다. "quqacukqauackck"과 같은 경우는 두 오리가 울었다고 볼 수 있다.

영선이가 녹음한 소리가 주어졌을 때, 영선이 방에 있을 수 있는 오리의 최소 개수를 구하는 프로그램을 작성하시오.


첫째 줄에 영선이가 녹음한 소리가 주어진다. 소리의 길이는 5보다 크거나 같고, 2500보다 작거나 같은 자연수이고, 'q','u','a','c','k'로만 이루어져 있다.


영선이 방에 있을 수 있는 오리의 최소 수를 구하는 프로그램을 작성하시오. 녹음한 소리가 올바르지 않은 경우에는 -1을 출력한다.

예제 1
quqacukqauackck

출력 1
2

예제 2
kcauq
출력 2
-1

예제 3
quackquackquackquackquackquackquackquackquackquack
출력 3
1

예제 4
qqqqqqqqqquuuuuuuuuuaaaaaaaaaacccccccccckkkkkkkkkk

출력 4
10

예제 5
quqaquuacakcqckkuaquckqauckack
출력 5
3

예제 6
quackqauckquack
출력 6
-1

"""
import sys
sys.stdin = open("input.txt","r")

sounds = list(input())
ans = 0

if sounds[0] != 'q' or sounds[-1] != 'k' or len(sounds) % 5:
    print(-1)
    exit()

def find_quack(start): # 여기서는 uack 찾는거라고 보면돼. 
    quack = 'quack'
    j = 0
    global ans

    new_duck = True
    for i in range(start,len(sounds)):
        if sounds[i] == quack[j]:  # sounds에 문자랑 quack의 문자가 같으면
            if sounds[i] == 'k':  # 그러다가 이제 현재 문자가 k이면
                if new_duck:  # 새로운 오리일 경우이고,
                    ans += 1 # 그 때 ans를 하나 늘려구고
                    new_duck = False  # 새로운 오리를 생성하지 마라

                j = 0   # 이어지는 q 찾기 - 새로운 오리가 아니라 현재값
                sounds[i] = 0  # sounds의 i값을 0으로 해서 q 찾기 해주고
                continue

            j += 1  # j를 늘려서 다음 quack을 찾으려고 함.
            sounds[i] = 0 # 이건 이제 문자를 이미 탐색했다. 이런 의미임.


for i in range(len(sounds) - 4): # 무조건 4빼주기 uack을 찾아야 해
    if sounds[i] == 'q':  # sounds[i] 가 q이면 quack찾는 함수로 보내버려
        find_quack(i)

# print(sounds)
if any(sounds) or ans == 0:  # sounds에 0이 있다는건 모든 문자를 탐색했다는 뜻. 다 짝이 있다는 뜻. sounds에 어떤 알파벳이라도 남아 있으면 -1을 리턴
    print(-1)
else:
    print(ans)


### any()는 리스트나 튜플과 같은 반복 가능한(iterable) 객체를 받아서 그 안에 **하나라도 True가 있으면 True**를 반환하고, **모두 False이면 False**를 반환하는 함수야.
    
