n = int(input())  # 숫자의 개수 n 입력
number_list = input()

# 숫자를 모두 합산하여 출력
total_sum = sum(map(int, number_list))
print(total_sum)