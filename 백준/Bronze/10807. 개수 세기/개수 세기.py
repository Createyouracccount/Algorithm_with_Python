num = int(input())
num_list = list(map(int, input().split()))
check_num = int(input())
result = 0

for i in range(len(num_list)):
    if num_list[i] == check_num:
        result += 1

print(result)