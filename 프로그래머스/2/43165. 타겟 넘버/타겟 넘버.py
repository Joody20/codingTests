def solution(numbers, target):
    answer = 0
    def dfs(cnt, cur_sum):
        if cnt == len(numbers):
            if cur_sum == target:
                return 1
            else:
                return 0
            
        return dfs(cnt + 1, cur_sum + numbers[cnt]) + dfs(cnt + 1, cur_sum - numbers[cnt])

    answer = dfs(0,0)
    return answer