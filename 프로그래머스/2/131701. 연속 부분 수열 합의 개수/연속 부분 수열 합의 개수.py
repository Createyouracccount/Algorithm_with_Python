def solution(elements):
    # set함수 사용해서 중복 제거하고 결과를 저장할 집합
    result_set = set()
    # 리스트의 길이는 미리 구해서 넣으면서 사용
    length = len(elements)
    
    # 길이가 1일 경우, 요소 자체를 집합에 추가 / 집합이라서 add 사용, append랑 헷갈리지말기
    if length == 1:
        result_set.add(elements[0])
    
    # 인덱스를 통해 리스트 순회하면서 부분합 구하기
    for i in range(length):
        sum_list = 0
        for j in range(i, i + length):
            idx = j % length
            
            sum_list += elements[idx]
            result_set.add(sum_list)
    
    return len(result_set)