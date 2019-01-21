str = bin(1103515245)
shift_list=[]
for i in range(len(str)):
    if str[-i]=="1":
        shift_list.append(i-1)

def find_n_v3(shift_list):
    n = 0
    result = "1"

    while (1):
        tmp = 0
        for i in shift_list:
            tmp = tmp + int(result + ("0" * i), 2)

        result = bin(tmp + 12345)[-36:]
        n += 1
        if n % 1000000==0:
            print(n," times tried")
        if (int(result, 2) == 1):
            break
    return n


print(find_n_v3(shift_list))