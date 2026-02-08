N,M = map(int,input().split())

matrix_A = []
matrix_B = []

for _ in range(N):
    num_A = list(map(int,input().split()))
    matrix_A.append(num_A)

for _ in range(N):
    num_B = list(map(int,input().split()))
    matrix_B.append(num_B)


res = [[] for _ in range(N)]

for i in range(N):
    for j in range(M):
        res[i].append(matrix_A[i][j] + matrix_B[i][j])


    
for r in res:
    print(" ".join(map(str,r)))