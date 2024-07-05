def solution(n):
    # 기본 케이스 처리
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # 피보나치 리스트 초기화
    fibo_list = [0] * (n + 1)
    fibo_list[0] = 0
    fibo_list[1] = 1

    # 피보나치 수 계산
    for i in range(2, n + 1):
        fibo_list[i] = fibo_list[i - 1] + fibo_list[i - 2]
        answer = fibo_list[i] % 1234567

    return answer