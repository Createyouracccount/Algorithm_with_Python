def solution(s):
    count = 0
    zero_count = 0
    
    while s != "1": # s가 1이 될 때 까지 반복문 진행한다.
        zero_count += s.count('0')
        s = s.replace('0', '') # 0을 공백으로 변환해서 0 제거
        s = bin(len(s))[2:] # bib함수 : 2진수로 변환, 0b가 붙으니까 그거 제거하려고 슬라이싱 사용
        count += 1
    
    return [count, zero_count]
