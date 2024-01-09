n, x = map(int, (input().split()))
j = list(map(int, input().split()))

for i in range(n):    
    if j[i] < x:

        print(j[i], end=" ")