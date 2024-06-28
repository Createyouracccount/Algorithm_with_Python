from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)
    sorted_counts = sorted(count.values(), reverse=True)
    # 개수 기준 내림차순 정렬, 가장 많은것부터 뽑으려고
    # 왜 굳이 sort 안 쓰고 sorted? : 새롭게 정렬된 리스트 뽑아서 그걸로 계산하려고
    # count함수를 사용하면 2:3, 3:2 이런식으로 결과가 나와서 그 중 개수만 가져가려고
    
    total = 0 # 선택한 귤의 총 개수
    result = 0 # 선택한 귤의 종류
    
    for cnt in sorted_counts:
        total += cnt
        result += 1
        if total >= k:
            break
    
    return result