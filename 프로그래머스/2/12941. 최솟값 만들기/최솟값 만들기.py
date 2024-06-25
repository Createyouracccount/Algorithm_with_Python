# A에서는 min값을 계속 뽑고 B에서는 max값을 계속 뽑아서 계산 한다.
# A랑 B의 배열 길이는 같다.

def solution(A,B):
    A.sort()
    B.sort(reverse=True) # 내림차순
    
    answer = 0
    for a in range(len(A)): # A의 배열 길이만큼 같으니까
        answer += A[a] * B[a]

    return answer