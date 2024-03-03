n = int(input())
# 위에 만들기
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# 아래 만들기
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))