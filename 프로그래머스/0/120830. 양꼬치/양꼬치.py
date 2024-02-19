def solution(n, k):
    a = 12000 * n
    b = 2000 * k
    c = n // 10
    
    answer = a + b - 2000*c
    
    return answer