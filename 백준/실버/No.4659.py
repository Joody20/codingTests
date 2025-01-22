"""
백준 실버 5 비밀번호 발음하기 : https://www.acmicpc.net/problem/4659

예제:
a
tv
ptoui
bontres
zoggax
wiinq
eep
houctuh
end

"""

import sys
sys.stdin = open("input.txt", "r")

aeiou = {'a','e','i','o','u'}

while True:
    words = input().rstrip()  # ㄹㅇ 개큰실수 split()으로 한 나 자신 개큰실수 strip()으로 했어야 됐어.
    if 'end' in words:
        break

    checked = 0 # 모음이 하나인지 체크하는
    cnt_alpha = 0 # 자음을 세는
    cnt_aeiou = 0  # 모음을 세는
    contrast = 0 # 같은 글자 2번 연속인지 or 자음/모음 3개이면 1로 하기

    for i in range(len(words)):
        if i > 0:  # 이것도 개큰실수 나는 i가 걍 len이라고 생각했어. 근데 이거 인덱스잖아. i > 0인건 일단 words의 길이가 1이상이라는 뜻이잖아. 즉, 길이가 2인것부터 시작한다는거야. 그 때 !! 그 때 !1
            if words[i] == words[i-1]:# 현재 word와 전 word가 같으면
                if words[i] != 'e' and words[i] != 'o': # 그 때, e나 o가 없으면 not accept에 해당하니까 contrast = 1로
                    contrast = 1
                    break
        if words[i] in aeiou: # 글자가 1개여도 일단 모음이 있으면
            checked = 1 # 모음 있음 checked = 1로
            cnt_aeiou += 1  # 모음 있으니까 1 더해주고
            cnt_alpha = 0 # 이 때는 모음 확인만 해주는거니까 자음은 일단 리셋으로
            if cnt_aeiou == 3:  # 만약 모음의 카운트가 3이면
                    contrast = 1 # contrast 1로
                    break
        else:  # 모음이 없고 이제 자음이 있는 거면
            cnt_aeiou = 0 # 모음은 리셋
            cnt_alpha += 1 # 자음을 세줌
            if cnt_alpha == 3: # 그 때, 자음의 개수가 3이면
                contrast = 1 # contrast 1로
                break

    if contrast != 1 and checked == 1: # 따라서, not accept에 대한 조건이 하나도 걸리지 않으며, 모음이 있다고 판단된 경우
        print(f"<{words}> is acceptable.") # accept하다
    else:  # 아닌 경우
        print(f"<{words}> is not acceptable.")  # not accept하다.
