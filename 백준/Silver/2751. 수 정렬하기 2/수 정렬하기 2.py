import sys

n = int(input())
m = []
for _ in range(n):
    m.append(int(sys.stdin.readline()))
    # input()과 sys.stdin.readline()은 차이가 존재한다.
    # input으로 할 때 안 되는데 sys.stdin.readline으로 수정하자 시간초과가 생기지 않음.
    # 파이썬의 input()과 sys.stdin.readline의 차이 때문에 생기게 된 오류이다.
    """ input()은 문자열 변환, 줄 바꿈 제거 등 추가적인 과정이 있고, 
    데이터가 하나 씩 버퍼에 들어가는 반면 sys.stdin.readline()은 문자열로 변환, 
    줄 바꿈 과정이 없으며 데이터가 한 번에 버퍼에 들어가므로 
    sys.stdin.readline()이 input() 보다 빠르다.
    출처 : https://hs-archive.tistory.com/35"""
m.sort()
# 파이썬 내장함수인 sort함수를 사용

for i in m:
    print(i)
