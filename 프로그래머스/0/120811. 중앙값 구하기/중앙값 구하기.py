import statistics

def solution(array):
    array.sort()
    restult = statistics.median(array)
    # sort()로 정렬 후 statistics의 median()을 사용하여 중앙값 구하기
    
    return restult