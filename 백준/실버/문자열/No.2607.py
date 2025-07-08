"""
백준 비슷한단어(실버2) : https://www.acmicpc.net/problem/2607

영문 알파벳 대문자로 이루어진 두 단어가 다음의 두 가지 조건을 만족하면 같은 구성을 갖는다고 말한다.

1.두 개의 단어가 같은 종류의 문자로 이루어져 있다.
2. 같은 문자는 같은 개수 만큼 있다.
예를 들어 "DOG"와 "GOD"은 둘 다 'D', 'G', 'O' 세 종류의 문자로 이루어져 있으며 양쪽 모두 'D', 'G', 'O' 가 하나씩 있으므로 이 둘은 같은 구성을 갖는다. 하지만 "GOD"과 "GOOD"의 경우 "GOD"에는 'O'가 하나, "GOOD"에는 'O'가 두 개 있으므로 이 둘은 다른 구성을 갖는다.

두 단어가 같은 구성을 갖는 경우, 또는 한 단어에서 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우에 이들 두 단어를 서로 비슷한 단어라고 한다.

예를 들어 "DOG"와 "GOD"은 같은 구성을 가지므로 이 둘은 비슷한 단어이다. 또한 "GOD"에서 'O'를 하나 추가하면 "GOOD" 과 같은 구성을 갖게 되므로 이 둘 또한 비슷한 단어이다. 하지만 "DOG"에서 하나의 문자를 더하거나, 빼거나, 바꾸어도 "DOLL"과 같은 구성이 되지는 않으므로 "DOG"과 "DOLL"은 비슷한 단어가 아니다.

입력으로 여러 개의 서로 다른 단어가 주어질 때, 첫 번째 단어와 비슷한 단어가 모두 몇 개인지 찾아 출력하는 프로그램을 작성하시오.


첫째 줄에는 단어의 개수가 주어지고 둘째 줄부터는 한 줄에 하나씩 단어가 주어진다. 모든 단어는 영문 알파벳 대문자로 이루어져 있다. 단어의 개수는 100개 이하이며, 각 단어의 길이는 10 이하이다.

입력으로 주어진 첫 번째 단어와 비슷한 단어가 몇 개인지 첫째 줄에 출력한다.

예제 1
4
DOG
GOD
GOOD
DOLL

"""
from collections import Counter
import sys
sys.stdin = open("input.txt","r")

N = int(input())

word = list(input())  # 첫번 째 단어
word_count = Counter(word)

words = [list(input()) for _ in range(N-1)]  # 비슷한 단어들을 찾을 후보 단어들
# print(words)
count = 0

for i in range(len(words)):
    new_count = Counter(words[i])

    diff = 0

    # print(word_count.keys())
    # print(new_count.keys())
    union_word = set(word_count.keys() | new_count.keys())  # 중복되는 알파벳 빼고 합치는거야
    # print(union_word)

    for char in union_word:  # 합친 word중에서 
        diff += abs(word_count[char] - new_count[char])  # abs는 숫자차이를 구할 때 씀. 아 절댓값을 리턴하니까 -1여도 1, -2여도 2인거임.
        # print(diff)

    if diff <= 2 and abs(len(word) - len(words)) <= 1:  #다른게 2개 이하고, 타겟 글자와 후보 글자의 길이가 1이거나 1보다 작으면
        count += 1  # 비슷한 단어인거니까 count 1씩 더해주기

print(count)