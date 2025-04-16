"""
철수는 친구들과 빙고 게임을 하고 있다. 철수가 빙고판에 쓴 수들과 사회자가 부르는 수의 순서가 주어질 때, 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지를 출력하는 프로그램을 작성하시오.

첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.

첫째 줄에 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력한다.

예제 1
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15


출력 1
15

"""
import sys
sys.stdin = open("input.txt","r")

bingos = [list(map(int,input().split())) for _ in range(5)]

nums = sum([list(map(int, input().split())) for _ in range(5)], []) # -> 2차원 배열인데.. 1차원 배열로 할 수 있나..?


def checked_bingo(bingo):
    count = 0

    for row in bingo:
        if row.count(0) == 5:
            count += 1

    for col in range(5):
        if [bingo[row][col] for row in range(5)].count(0) == 5:
            count += 1

    if [bingo[i][i] for i in range(5)].count(0) == 5:
        count += 1

    if [bingo[i][4-i] for i in range(5)].count(0) == 5:
        count += 1

    return count

    

for idx, call in enumerate(nums):
    for i in range(5):
        for j in range(5):
            if bingos[i][j] == call:
                bingos[i][j] = 0

    if checked_bingo(bingos) >= 3:
        print(idx+1)
        break


    
