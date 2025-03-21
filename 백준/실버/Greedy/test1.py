"""
각 자리가 숫자로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 ‘x’ 혹은 ‘+’연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰수를 구하는 프로그램을 작성하세요.

단 , +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산을 왼쪽부터 순서대로 이루어진다고 가정한다.

** 두 수에 대하여 연산을 수행할 때, 두 수 중에서 하나라도 1이하인 경우에는 더하며 두 수가 모두 2이상인 경우에는 곱하면 정답입니다.
"""
#02984
import sys
sys.stdin = open("input.txt","r")


nums = input()
result = int(nums[0])

for i in range(1,len(nums)):
    num = int(nums[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
    
print(result)
