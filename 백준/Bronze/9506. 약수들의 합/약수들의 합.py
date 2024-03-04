while True:
    n = int(input())
    yaksoo_list = []
    if n == -1:
        break
    else:
        for i in range(1, int(n**(1/2)) + 1):
            if n % i == 0:
                yaksoo_list.append(i)
                if i**2 != n:
                    yaksoo_list.append(n // i)

        yaksoo_list.sort()

        del yaksoo_list[-1] # 마지막 약수 제거
        perfect_num = sum(yaksoo_list) # 마지막 약수 제거 후 총 합을 더함

        if perfect_num == n: # 만약 완전수가 입력값과 같다면
            print(f"{n} =", end=" ")
            for k in range(len(yaksoo_list) - 1): # 마지막 약수를 제외하고 출력
                print(yaksoo_list[k], end=" + ")
            print(yaksoo_list[-1]) # 마지막 약수 출력 (뒤에 + 없이)
        else:
            print(f"{n} is NOT perfect.")