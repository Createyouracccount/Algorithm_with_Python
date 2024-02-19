def solution(n):
    result = n ** 0.5 # n을 1/2 제곱하면 제곱근을 구할 수 있다.
    if result.is_integer(): # is_integer를 사용해서 정수인지 아닌지 확인한다.
        return 1 # 정수라면 1을 리턴하면 되고
    else:
        return 2 # 정수 아니면 2를 리턴하면 된다.