"""
백준 브론즈 2 : 복호화 > 가장 빈번하게 나타나는 알파벳을 리턴하고, 빈도수가 여러개이면 ?을 리턴함.
"""
from collections import Counter  # 내가 썼었던 Counter 메소드를 활용했다. ㄹㅈㄷ 
import sys
sys.stdin = open("input.txt", "r")


N = int(input())

words = [(input().strip().replace(" ","")) for _ in range(N)]


for w in words:
    count = Counter(w)  # 일단 알파벳들의 count를 구해서 
    most_common = count.most_common(2)  # 나는 이제 가장 count가 많은 걸 구하는 코드를 몰랐다, 그건 most_common 메소드를 썼었으면 됐다 !!!!! 이걸 2개 가져와서

    if len(most_common) < 2:  # 이게 킥이였다. 계속 indexError 가 났는데 이유를 몰랐다. 근데 most_common이 2개가 아닐수도 있을거라는 생각을 못했다.... 구래서 미리 위에서 2개를 가져오고 길이가 2보다 작으면 그냥 제일 count가 높은 알파벳을 가져오고
         print(most_common[0][0])  
    elif most_common[0][1] == most_common[1][1]:  # count의 개수가 같으면 ?를 리턴
         print('?')
    else:  # 아무것도 아니면 이제 가장 count가 높은 알파벳을 가져오면 된다.
         print(most_common[0][0])
    

"""
>> 내가 잘못 했던 코드
from collections import Counter
import sys

N = int(input())

words = [(input().strip().replace(" ","")) for _ in range(N)]

for w in words:
    count = Counter(w)

    if count.most_common(1)[0][1] == count.most_common(2)[1][1]:  # 여기서 에러가 났던건데, 2번째가 없을수도 있자나. 그걸 생각못했어ㅠㅠ
        print('?')
    else:
        print(count.most_common(1)[0][0])

"""



