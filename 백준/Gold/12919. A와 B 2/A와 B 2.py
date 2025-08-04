S = input()
T = input()

def dfs(T):
    if T == S:
        print(1)
        exit()

    if len(T) == 0:
        return 0
    
    if T[-1] == 'A':  # 맨 뒤 문자가 A이면,
        dfs(T[:-1])  # 제거해서 재귀

    if T[0] == 'B': # 처음문자가 B이면,
        dfs(T[1:][::-1])

dfs(T)
print(0)