S = input()
P = input()

idx = 0 # S의 인덱스
count = 0 # 몇 번 복사했는지 세는 변수
    
    
    # S의 모든 부분 문자열을 집합에 저장 한 후에 
substring = set()
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        substring.add(S[i:j])

while idx < len(P):
    for i in range(len(P),0,-1):
        if P[idx:idx + i] in substring: # P의 idx부터 idx + i까지의 부분 문자열이 substring에 존재하면
            idx += i # idx에 i를 더해서 idx값을 업데이트 해주고  
            count += 1 # count 늘려줌
            break


print(count)