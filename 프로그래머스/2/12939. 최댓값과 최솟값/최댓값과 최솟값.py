def solution(s):
    # 문자열을 공백을 기준으로 분리하여 리스트로 변환한다.
    numbers = list(map(int, s.split()))
    
    # 최소값과 최대값 찾기 min, max 함수 사용
    min_val = min(numbers)
    max_val = max(numbers)
    
    # "(최소값) (최대값)" 형태의 문자열로 반환하여 구한다.
    return f"{min_val} {max_val}"