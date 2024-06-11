
def solution(people, limit):
    # 사람들의 몸무게를 오름차순으로 정렬
    people.sort()
    
    left = 0
    right = len(people) - 1
    boats = 0
    
    while left <= right:
        # 가장 가벼운 사람과 가장 무거운 사람이 함께 탈 수 있는지 확인
        if people[left] + people[right] <= limit:
            left += 1 
        right -= 1
        # 보트의 수를 증가
        boats += 1
    
    return boats