def solution(money):  
    coffee = money // 5500
    change = money - coffee*5500
    answer = [coffee, change]
    return answer