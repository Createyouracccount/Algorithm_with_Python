n = int(input())
m = list(map(int, input().split()))

if n in m:
    print(m.count(n))
else:
    print(0)