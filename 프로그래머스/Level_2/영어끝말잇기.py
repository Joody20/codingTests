"""
프로그래머스 level2 : https://school.programmers.co.kr/learn/courses/30/lessons/12981

1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있습니다. 영어 끝말잇기는 다음과 같은 규칙으로 진행됩니다.

1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
이전에 등장했던 단어는 사용할 수 없습니다.
한 글자인 단어는 인정되지 않습니다.
다음은 3명이 끝말잇기를 하는 상황을 나타냅니다.

tank → kick → know → wheel → land → dream → mother → robot → tank

위 끝말잇기는 다음과 같이 진행됩니다.

1번 사람이 자신의 첫 번째 차례에 tank를 말합니다.
2번 사람이 자신의 첫 번째 차례에 kick을 말합니다.
3번 사람이 자신의 첫 번째 차례에 know를 말합니다.
1번 사람이 자신의 두 번째 차례에 wheel을 말합니다.
(계속 진행)
끝말잇기를 계속 진행해 나가다 보면, 3번 사람이 자신의 세 번째 차례에 말한 tank 라는 단어는 이전에 등장했던 단어이므로 탈락하게 됩니다.

사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution 함수를 완성해주세요.

***출력
정답은 [ 번호, 차례 ] 형태로 return 해주세요.
만약 주어진 단어들로 탈락자가 생기지 않는다면, [0, 0]을 return 해주세요.



n	words	result
3	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	[3,3]
5	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]	[0,0]
2	["hello", "one", "even", "never", "now", "world", "draw"]	[1,3]

"""

def solution(n, words):
    answer = []
    speaked_words = [words[0]]  # 첫 시작 단어는 넣고
    
    
    for i in range(1,len(words)):  # 다음 숫자부터 하는거야
        if words[i-1][-1] == words[i][0] and words[i] not in speaked_words:
            speaked_words.append(words[i])
        else:
            break
            
    for i in range(0,len(words),n):
        origin = len(words[i:i+n])
        change = len(speaked_words[i:i+n])   # 지금 행이 차례야, 열이 번호고
        
        if origin != change:
            num = (i + change) % n + 1  #change에서 틀린 그 열의 번호를 알고 싶었어. i + change % n + 1
            idx = i // n + 1  # 틀린 행의 번호 
            answer.append((num,idx))
            
    if len(answer) == 0:
        return [0,0]
    else:
        return answer[0]
    