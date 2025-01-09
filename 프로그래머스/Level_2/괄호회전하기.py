def solution(s):
    def valid(string):
        res = [] # 이건 이제 올바른 괄호인지를 판단하기 위한 새 배열
        matching = {')':'(' , ']' : '[' , '}' : '{' }
        for i in string:
            if i in matching.values():
                res.append(i)
            elif i in matching.keys():
                if not res or res[-1] != matching[i]: # 맞지 않거나 res가 비어 있을 때는 false 리턴
                    return False
                res.pop() # 맞으면 빼버려
        return len(res) == 0 # res가 비어져 있으면 올바른괄호끼리된것임 !!!!
    

    count =  0 # 올바른 괄호 문자열 일 때 count 세는거..

    for _ in range(len(s)):
        s = s[1:] + s[0] # 첫번째 요소를 맨뒤로 보내는
        if valid(s): # 그걸 저 함수로 보내고
            count += 1 # 맞으면 count 증가
            
    return count 