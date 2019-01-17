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
    counter = [0]*4
    for i in range(length):
        mod = num%(10**((length-i)-1))
        num = num - mod
        print("mod = ",mod)
        counter[i] = num/(10**((length-i)-1))
        num = mod

        print(counter[i])
    four = {3:"MMM",2:"MM",1:"M",0:""}
    three = {9:"CM",8:"DCD",7:"DCC",6:"DC",5:"D",4:"CD",3:"CCC",2:"CC",1:"C",0:""}
    two = {9:"XC",8:"LXXX",7:"LXX",6:"LX",5:"L",4:"XL",3:"XXX",2:"XX",1:"X",0:""}
    one = {9:"IX",8:"VIII",7:"VII",6:"VI",5:"V",4:"IV",3:"III",2:"II",1:"I",0:""}
    result+= four[counter[0]]+three[counter[1]]+two[counter[2]]+one[counter[3]]

    return result
num =1904
print(ten_to_rome(num))

