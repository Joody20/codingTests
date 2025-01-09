def solution(clothes):
    # 의상의 종류를 그룹화하기 위해 딕셔너리를 선언
    clothes_dict = {}  
    for item, Type in clothes:
        if Type not in clothes_dict:
            clothes_dict[Type] = []  # 새로운 리스트 생성
        clothes_dict[Type].append(item)  # 아이템을 해당 타입의 리스트에 추가
        
    # 가능한 내가 입을 수 있는 조합의 수...
    total_clothes = 1
    for group in clothes_dict.values(): # 의상의 이름을 그룹
        total_clothes *= (len(group)+1) # 아무것도 선택하지 않음의 + 1인거야..
        print(total_clothes)
        print(group)
        
    total_clothes -= 1; # 아무것도 착용하지 않을일은 없으니까 -1 !
    
    return total_clothes
        
    
