n = list(map(int, input().split()))

x = n[0]
y = n[1]
w = n[2]
h = n[3]

left = x
right = w - x
top = h - y
bottom = y

min_dist = min(left, right, top, bottom)

print(min_dist)