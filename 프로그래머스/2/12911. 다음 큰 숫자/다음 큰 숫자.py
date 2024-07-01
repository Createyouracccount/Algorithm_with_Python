def solution(n):
    # n의 2진수에서 1의 개수
    num_bin_one = bin(n).count('1')
    
    # n보다 큰 숫자부터 시작해서 반복문 돌리기
    next_num = n + 1
    while True:
        # 다음 숫자의 2진수에서 1의 개수
        next_num_bin_one = bin(next_num).count('1')
        
        # 1의 개수가 같으면 결과 반환
        if next_num_bin_one == num_bin_one:
            return next_num
        
        # 조건을 만족하지 않으면 다음 숫자로 증가
        next_num += 1
