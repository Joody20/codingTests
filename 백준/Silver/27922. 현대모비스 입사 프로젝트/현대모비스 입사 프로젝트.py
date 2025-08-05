N,K = map(int,input().split())
lectures = [tuple(map(int,input().split())) for _ in range(N)]

max_result = 0

for i,j in [(0,1), (1,2),(0,2)]:
    sorted_lectures = sorted(lectures, key=lambda x: x[i] + x[j], reverse=True)

    A = B = C = 0
    for a,b,c in sorted_lectures[:K]:
        A += a
        B += b
        C += c

    max_result = max(max_result, A + B, B + C, A + C)

print(max_result)