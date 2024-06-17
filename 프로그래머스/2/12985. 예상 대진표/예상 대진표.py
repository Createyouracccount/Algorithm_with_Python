def solution(n,a,b):
    round_num = 0
    
    # 참가자가 서로 만날 때까지 반복
    while a != b:
        # 다음 라운드 번호 갱신
        a = (a + 1) // 2
        b = (b + 1) // 2
        round_num += 1
    
    return round_num