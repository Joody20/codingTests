import re
import sys
sys.stdin = open("input.txt","r")

file = input()
find_w = input()

# find_w랑 file에 있는 단어가 똑같으면 -> 이거에 대한 함수가 존재, import re re.findall(비교하고자하는문자열, 찾아야하는 문자열)
# 겹치지 않고 찾을 때!!!! 이건 중복되는 인덱스를 가지면 안되거든. 그 때는 re.findall(word,words)
matches = re.findall(find_w,file)

print(len(matches))
