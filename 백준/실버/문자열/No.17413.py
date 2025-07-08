"""
백준 실버 3 단어뒤집기 2 : https://www.acmicpc.net/problem/17413


예제 :
baekjoon online judge
<open>tag<close>
<ab cd>ef gh<ij kl>
one1 two2 three3 4fourr 5five 6six
<int><max>2147483647<long long><max>9223372036854775807
<problem>17413<is hardest>problem ever<end>
<   space   >space space space<    spa   c e>
"""

import sys
sys.stdin = open("input.txt", "r")


words = input()

ans = "" # 문자를 이어 붙힐거야 여기에
i = 0 # 현재 위치


while i < len(words):
    start = words.find("<", i)  # "<" 의 시작점 위치
    if start == -1: # 더이상 <이 없으면 종료
        res = []

        for word in words[i:].split():   # 이게 이제 <>가 없을 때 역순으로 한다는거 아니야?
            res.append(word[::-1])

        ans += ' '.join(res)
        break

    end = words.find(">",start)  # > 문자열 찾음.

    res = [] # 같은 배열에 

    for word in words[i:start].split():  # 현재 i 위치와 start 까지 split해서 
        res.append(word[::-1]) # 태그 외부 문자열은 역순으로

    ans += ' '.join(res)

    ans += words[start:end+1] # 태그 내부 문자열은 그대로

    i = end + 1


print(ans)



# for w in wordss:
#     res.append(w[::-1])

# print(' '.join(res))


# start = words.find(">") + 1
# end = words.find("<",start)

# print(words[start:end])



# <>가 있다면,, 이 태그 안에 있는 단어만,,, 뒤집어야되는데,,,,,


# for w in words:
    # result = w.split(">")[1].split("<")[0]
    # print(result[::-1])
  
    