def max_profit(n, days):
    mx_pf = [0] * (n + 1)  # mx_pf[i]: i일까지 상담을 진행했을 때의 최대 이익
    # 각 날짜마다 상담을 진행했을 때의 최대 이익을 저장한다.

    for i in range(1, n + 1):
        # i일에 상담을 할 경우
        if i + days[i][0] - 1 <= n:  # 상담을 끝까지 할 수 있는지 확인한다.
            mx_pf[i + days[i][0] - 1] = max(mx_pf[i + days[i][0] - 1], mx_pf[i - 1] + days[i][1])
        
        # i일에 상담을 안 할 경우
        mx_pf[i] = max(mx_pf[i], mx_pf[i - 1])

    return mx_pf[n]

def main():
    n = int(input())
    days = [(0, 0)]  # 0번째 인덱스를 무시하기 위해 추가 
    for _ in range(n):
        T, P = map(int, input().split())
        days.append((T, P))

    print(max_profit(n, days))

if __name__ == "__main__":
    main()