def four_to_ten(num):

    result = 0
    length = len(num)
    for i in range(length):
        if (num[i]!="1" and num[i]!="2" and num[i]!="3" and num[i]!="0"):
            print("not a four step number: ",num[i])
            return
        result += int(num[i])*(4**(length-i-1))
    return result

#number = input("your number:")
#print(four_to_ten(number))

def alpha_to_ten(str):
    result = 0
    eight = [""]*len(str)
    for i in range(len(str)):
        eight[i]=ord(str[i])-ord("a") #ord(): the ASCII of a char
        result += int(eight[i])*(8**(len(str)-i-1))
    return result

#print(alpha_to_ten("bcd"))
#I=1 V=5 X=10 L=50 C=100 D=500 M=1000 big to small
#can't use four same rome alpha at same time
#IV = 4 IX = 9
#XL = 40 XC = 90
#CD = 400 CM = 900
#2015 = MMXV
#0<=num<=4000 max:MMMM
def rome_to_ten(str):
    value={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    result = 0
    length = len(str)
    i = 0
    while i<length:
        print("i = %r, str[%r] = %r"%(i,i,str[i]))
        if i<=length-1 and (str[i:i+2]=="CM" or str[i:i+2]=="CD" or str[i:i+2]=="XL" or str[i:i+2]=="XC" or str[i:i+2]=="IX" or str[i:i+2]=="IV"):
            print("found a special number ",str[i:i+2])
            result+=value[str[i+1]]-value[str[i]]
            print("result = ",result)
            i = i+2
        else:
            result+=value[str[i]]
            print("str[%r]:%r" % (i,str[i]))
            i+=1
    return result
#print(rome_to_ten("MCMIV"))

#0<=num<=4000
def ten_to_rome(num):
    result=""
    length = len(str(num))
    for i in range():

    return result
num =1000
print(len(str(num)))
print(len(num))
