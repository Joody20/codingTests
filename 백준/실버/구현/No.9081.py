"""
백준 실버 1 : 단어 맞추기 https://www.acmicpc.net/problem/9081
(사전순 조합 찾기 알고리즘)

입력의 첫 줄에는 테스트 케이스의 개수 T (1 ≤ T ≤ 10)가 주어진다. 각 테스트 케이스는 하나의 단어가 한 줄로 주어진다. 단어는 알파벳 A~Z 대문자로만 이루어지며 항상 공백이 없는 연속된 알파벳으로 이루어진다. 단어의 길이는 100을 넘지 않는다.

각 테스트 케이스에 대해서 주어진 단어 바로 다음에 나타나는 단어를 한 줄에 하나씩 출력하시오. 만일 주어진 단어가 마지막 단어이라면 그냥 주어진 단어를 출력한다.

예제 1
4
HELLO
DRINK
SHUTTLE
ZOO

출력 1
HELOL
DRKIN
SLEHTTU
ZOO

"""
import sys
sys.stdin = open("input.txt","r")

T = int(input())

for _ in range(T):
    words = list(input())

    i = len(words) - 2

    # 1. 뒤에서 부터 i를 찾기
    while i >=0 and words[i] >= words[i+1]:
        i -= 1

    if i == -1:
        print("".join(words))
        continue

    # 2. i보다 뒤에서 word[i]보다 큰 가장 작은 j를 찾기
    j = len(words) - 1
    while words[j] <= words[i]:
        j -= 1

    # 3. 둘 바꾸기
    words[i], words[j] = words[j] , words[i]

    words[i+1:] = sorted(words[i+1:]) 


    print("".join(words))

    

    