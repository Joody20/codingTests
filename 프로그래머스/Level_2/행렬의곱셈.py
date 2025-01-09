def solution(arr1, arr2):



# # arr 1 = 1행이랑 arr2 = 1열을 곱해
# 2*5 + 3*2  + 2*3  == 22
# # arrr 1 = 1행 arr 2 = 2열을 곱해
# 2*4 + 3*4 + 2*1 == 22
# # arr 1 = 1행 arr2 = 3열을 곱해
# 2*3 + 3*1 + 2*1 == 11

# -> 이런식으로 하면 되는데요 !!!
    rows_1 = len(arr1)  # arr1의 행 
    cols_1 = len(arr1[0]) # arr1의 열
    cols_2 = len(arr2[0]) # arr2의 열
    
    result = [[0 for _ in range(cols_2)] for _ in range(rows_1)]
    
    
    for row in range(rows_1):
        for col in range(cols_2):
            for i in range(cols_1):
                result[row][col] += arr1[row][i] * arr2[i][col]
    return result
                
    



