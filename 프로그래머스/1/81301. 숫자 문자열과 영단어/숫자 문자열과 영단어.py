def solution(s):
    answer = s
    num_spell = { 'zero' : '0', 'one' : '1' , 'two' : '2', 'three' : '3', 'four' : '4', 'five': '5',
                'six' : '6', 'seven': '7', 'eight':'8', 'nine':'9'}

    
    for word in num_spell.keys():
        if word in s:
            answer = answer.replace(word, num_spell.get(word))
            

    return int(answer)