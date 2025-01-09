from collections import deque

def solution(x, y, n):
    d = [0] * 10000001  # d에 0으로 된 배열 하나를 만들어
    q = deque()  # deque로 선언하고
    d[x] = 1 # 첫번째에 1로 해줘 왜냐 1보다 커야 되니ㄲ
    q.append(x)
    
    while q:
        x = q.popleft()
        if 1 <= x + n <= 1000000 and d[x + n] == 0:
            d[x + n] = d[x] + 1
            q.append(x + n)  
        if 1 <= x * 2 <= 1000000 and d[x * 2] == 0:
            d[x * 2] = d[x] + 1
            q.append(x * 2)
        if 1 <= x * 3 <= 1000000 and d[x * 3] == 0:
            d[x * 3] = d[x] + 1
            q.append(x * 3)
            
    return d[y] - 1
            
    
    