import sys
sys.stdin = open("input2.txt", "r")

def word_fix(word):
    for i in word:
        res = i.replace('a',"").replace('e',"").replace('i',"").replace('o',"").replace('u',"")
        ans.append(res)

T = int(input().strip())

for test_case in range(1, T+1):
    word = input()
    
    ans= []
    word_fix(word)
    print(f'#{test_case} {"".join(ans)}')