import sys
sys.stdin = open("input.txt","r")
from bisect import bisect_left , bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_index(array, left, right):
    right_index = bisect_right(array, right)
    left_index = bisect_left(array , left)
    return right_index - left_index

N , x = map(int,input().split())
array = list(map(int,input().split()))


count = count_index(array, x , x)

if count == 0:
    print(-1)
else:
    print(count)