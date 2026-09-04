def solution(n, left, right):
    answer = []
    
    for i in range(left,right + 1):
        answer.append(max(i//n, i%n) + 1)
        
#     arr = [[0]*n for _ in range(n)]
    
#     for i in range(1,n+1):
#         for row in range(i):
#             for col in range(i):
#                 if arr[row][col] == 0:
#                     arr[row][col] = i
    
#     answer = [num for a in arr for num in a]
    
#     # print(answer)
            
#     answer = answer[left: right+1]


    return answer