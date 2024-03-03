a=int(input())
b=1000-a
cnt=0

li=[500,100,50,10,5,1]

for i in li:
    cnt+=b//i
    b%=i
print(cnt)