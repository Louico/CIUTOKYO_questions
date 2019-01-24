import numpy as np
def cal_store(n):
    store=[0]*(n+1)
    for i in range(n+1):
        if i <= 2:
            store[i] = 1
        else:
            store[i] = store[i-1] + store[i-2]
    return store[n]
def cal_fast(n):
    result =  [1,1],[1,0]
    factor = [1,1],[1,0]
    bin_num = bin(n-1)
    #print("bin is ",bin_num)
    f_list =[]
    #for i in range(n-1):
    #    result = np.dot(result,factor)

    for i in range(len(bin_num)):
        if bin_num[i] == "1":
            k = len(bin_num)-i-1
            f = [1,1],[1,0]
            #print("the bin_num is ",bin_num,"current k in bin is","1"+"0"*k)
            for j in range(int("1"+"0"*k,2)-1):

                f = np.dot(f,factor)
            #print("the ",int("1"+"0"*k,2),"times f is ",f)
            f_list.append(f)
    for i in f_list:
        #print("doing ",result,"dot ",i)
        result = np.dot(result,i)
        #print("the result of the action is ",result)


    #print(result)
    return result[1][0]


def cal_test(n):
    result = [1,1],[1,0]
    for i in range(n-1):
        result = np.dot(result,([1,1],[1,0]))
    #print(result)
    return result[1][0]
#print(cal_r(50))
#print(cal_store(140))
#print(cal_fast(140))
#print(cal_test(140))
#print(len(str(cal_store(140))))
#print(cal_store(100))
def long_add(a1,a2):
    a1 = int(a1,10)
    a2 = int(a2,10)
    return a1+a2

def float_32(a1,a2):
    b1,p1 = a1.split(" ")
    b2,p2 = a2.split(" ")
    first = int(b1)*int(b2)
    power = str(int(p1) + int(p2))
    if len(power) == "1":
        power = "0" + power

    result = (str(first))[:32]+" "+str(power)
    return result
"""
a = "12345678901234567890123456789012 04"
b = "98765432109876543210987654321098 09"
#print(float(a,b))
#w,_ = float(a,b).split(" ")
#print(len(w))
t1 = "15"+"0"*30+" 02"
t2 = "2"+"0"*31+" 04"
print(float(t1,t2))
w,_ = float(t1,t2).split(" ")
result = int(w) * (10**(-31+int(_)))
print(result)
"""
sqrt_five = format(np.sqrt(5)+1,".32g")
sqrt_five = (sqrt_five.split(".")[0]+sqrt_five.split(".")[1])[:32]+" 00"
a = "1"+"0"*31+" 00"
b = "05"+"0"*30+" 00"
result = float_32(sqrt_five,b)
print(result)
print((np.sqrt(5)+1)/2)
