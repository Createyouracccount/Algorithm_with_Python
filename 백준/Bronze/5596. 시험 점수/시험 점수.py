a=list(map(int, input().split()))
b=list(map(int, input().split()))
A=sum(a)
B=sum(b)
if A>B:
    print(A)
else:
    print(B)