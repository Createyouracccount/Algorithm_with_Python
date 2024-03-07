n = int(input())
num = list(map(int, input().split())) # 일단 숫자를 나눠서 입력 받고
avg_list = [] # 리스트를 만들어서 새롭게 계산 될 값을 담을 수 있도록 만들고
for i in range(n):
    num_max = max(num)  # 최댓값 찾고
    avg_list.append((num[i] / num_max) * 100) # num[1] = 1 num[2] = 100 num[3] = 100 num[4] = 100 일 때 최댓값에서 나누고 100 곱해주고 
    
avg_sum = sum(avg_list) # 새롭게 만든 리스트 내부 값의 총합을 구하고
avg_real = avg_sum / n  # 입력 값으로 나눠준다.
print(avg_real)