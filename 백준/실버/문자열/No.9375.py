"""
백준 실버 3(자료구조) : 패션왕 신해빈

예제
2
3
hat headgear     -> hat , sunglasses , turban , hat/sunglasses , sunglasses/turban
sunglasses eyewear
turban headgear
3
mask face   -> 여기는 지금 다 같은 거니까 mask , sunglasses , makeup
sunglasses face
makeup face
"""

import sys
sys.stdin = open("input.txt", "r")

N = int(input())  # 케이스 수

index = 1    # 읽을 줄의 인덱스

for _ in range(N):
    item_count = int(input())  # 현재 그룹의 아이템 개수
    index += 1
    group = [tuple(input().split()) for _ in range(index , index + item_count)]  # 1부터 1 + 3 하면 1~4이니까 

    cloths_dict = {}


    for item, type in group:
        if type not in cloths_dict:
            cloths_dict[type] = []
        cloths_dict[type].append(item)

    count = 1

    for group in cloths_dict.values():
        count *= (len(group)+1)

    count -= 1

    print(cloths_dict)
    print(count)


