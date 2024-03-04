a = int(input())
b = int(input())
c = int(input())
mul = list(map(int, str(a*b*c)))

for i in range(10):
    cnt = mul.count(i)
    print(cnt, sep='\n')