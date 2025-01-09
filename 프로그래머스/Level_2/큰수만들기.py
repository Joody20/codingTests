def solution(number, k):
    nums = list(number)
    stack = []
    
    for num in nums:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
        print(stack)
    
    while k > 0:
        stack.pop()
        k -= 1
    return ''.join(stack)
        