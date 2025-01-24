"""
백준 실버 4 : https://www.acmicpc.net/problem/1764
"""


import sys
sys.stdin = open("input.txt", "r")

N , M = map(int,input().split())  # N은 듣도 못한 사람의 수 , M은 보도 못한 사람의 수  

N_person = set(input().strip() for _ in range(N))   # ****set을 사용하게 되면 내가 방금처럼 for _ in range(N+2,N+M+2) 하지 않아도 N개의 개수만큼
M_person = set(input().strip() for _ in range(M)) # M개의 개수 만큼 반복문으로 input파일에서 가져올 수 있음 !!!!

res = sorted(N_person & M_person)  # 교집합을 사용할 수 있었음....썅.... & 중복이 되는 걸 고를 때 "&"를 사용해야겟다.


print(len(res))
print("\n".join(res))


"""
잘못한 코드  -> 처음엔 이제 if N_person[i] == M_person[j]: 이런 로직을 생각했지만 ? 너무 쉬운 "&"이 있엇었음.....
N , M = map(int,input().split())  # N은 듣도 못한 사람의 수 , M은 보도 못한 사람의 수  

N_person = [input().strip() for _ in range(N)]  
M_person = [input().strip() for _ in range(N+2 , N + M + 2)]

res = []

for i in range(N):
    for j in range(M):
        if N_person[i] == M_person[j]:
            res.append(N_person[i])


print(len(res))
print("\n".join(res))

"""

