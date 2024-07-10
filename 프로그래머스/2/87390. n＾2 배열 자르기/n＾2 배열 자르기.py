def solution(n, left, right):
    result = []

    for k in range(left, right + 1):
        x = k // n
        y = k % n
        result.append(max(x, y) + 1)

    return result