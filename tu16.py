rowtype1 = "****"
rowtype2 = "|  |"
rowtype3 = "*  *"
rowtype4 = "*"
rowtype5 = "|"
rowtype6 = "   |"
rowtype7 = "|   "
rowtype8 = "*   "
rowtype9 = "   *"

def number(numbers):
    r= [""]*5
    for i in numbers:
        if i=="0":
            r[0]+=rowtype1
            r[1]+=rowtype2
            r[2]+=rowtype3
            r[3]+=rowtype2
            r[4]+=rowtype1
        if i=="1":
            r[0] += rowtype4
            r[1] += rowtype5
            r[2] += rowtype4
            r[3] += rowtype5
            r[4] += rowtype4
        if i=="2":
            r[0] += rowtype1
            r[1] += rowtype6
            r[2] += rowtype1
            r[3] += rowtype7
            r[4] += rowtype1
        if i=="3":
            r[0] += rowtype1
            r[1] += rowtype6
            r[2] += rowtype1
            r[3] += rowtype6
            r[4] += rowtype1
        if i=="4":
            r[0] += rowtype3
            r[1] += rowtype2
            r[2] += rowtype1
            r[3] += rowtype6
            r[4] += rowtype9
        if i=="5":
            r[0] += rowtype1
            r[1] += rowtype7
            r[2] += rowtype1
            r[3] += rowtype6
            r[4] += rowtype1
        if i=="6":
            r[0] += rowtype8
            r[1] += rowtype7
            r[2] += rowtype1
            r[3] += rowtype2
            r[4] += rowtype1
        if i=="7":
            r[0] += rowtype1
            r[1] += rowtype6
            r[2] += rowtype9
            r[3] += rowtype6
            r[4] += rowtype9
        if i=="8":
            r[0] += rowtype1
            r[1] += rowtype2
            r[2] += rowtype1
            r[3] += rowtype2
            r[4] += rowtype1
        if i=="9":
            r[0] += rowtype1
            r[1] += rowtype2
            r[2] += rowtype1
            r[3] += rowtype6
            r[4] += rowtype9
        for i in range(len(r)):
            r[i]+="  "
    emoji = r[0]+"\n"+r[1]+"\n"+r[2]+"\n"+r[3]+"\n"+r[4]

    return (emoji)
"""
num = input("please input the number to be print ")
print(number(num))
output_path = "./out1.txt"

with open(output_path,"w") as f:
    f.write(number(num))


with open("out1.txt","r") as f:
    text = f.read()
    numlist = text.split("\n")
    result = ""

    for i in range(len(numlist[0])):
        if numlist[0][0:3]=="*  ":
            if numlist[2][0:3]=="*  ":
                result += "1"
                for i in range(len(numlist)):
                    numlist[i] = numlist[i][3:]
        if numlist[0] =="":
            break

        else:
            if numlist[0][0:4] == "****":
                if numlist[1][0:4]=="   |":
                    if numlist[2][0:4]=="****":
                        if numlist[3][0:4]=="|   ":
                            result+="2"
                        if numlist[3][0:4]=="   |":
                            result += "3"
                    if numlist[2][0:4]=="   *":
                        result+="7"
                if numlist[1][0:4]=="|  |":
                    if numlist[2][0:4]=="****":
                        if numlist[3][0:4]=="|  |":
                            result+="8"
                        if numlist[3][0:4]=="   |":
                            result+="9"
                    if numlist[2][0:4]=="*  *":
                        result+="0"
                if numlist[1][0:4]=="|   ":
                    result += "5"
            if numlist[0][0:4] == "*   ":
                result+="6"
            if numlist[0][0:4] =="*  *":
                result +="4"
            for i in range(len(numlist)):
                numlist[i] = numlist[i][6:]
print(result)

"""


def numberC(num):
    num = num.split(",")
    numbers = num[0]
    maxtrace = 0
    max = num[2]
    while 2*maxtrace+2<len(num):
        if max < num[2*maxtrace+2]:
            max = num[2*maxtrace+2]
        maxtrace+=1
    size = int(max)+5
    print("row size = ",size)
    r= [""]*size
    for i in range(len(numbers)):
        offside = int(num[2 * i + 1])
        print(offside)
        print("add number ",numbers[i])
        if numbers[i]=="1":
            r[0+offside] += rowtype4
            r[1+offside] += rowtype5
            r[2+offside] += rowtype4
            r[3+offside] += rowtype5
            r[4+offside] += rowtype4
            for l in range(0+offside):
                r[l] += " "
            for l in range(size-4-offside-1):
                r[l+4+offside+1]+=" "

        if numbers[i]=="0":
            r[0+offside]+=rowtype1
            r[1+offside]+=rowtype2
            r[2+offside]+=rowtype3
            r[3+offside]+=rowtype2
            r[4+offside]+=rowtype1
            for l in range(0+offside):
                r[l] += " "*4
            for l in range(size-4-offside-1):
                r[l+4+offside+1]+=" "*4
        if numbers[i]=="2":
            r[0+offside] += rowtype1
            r[1+offside] += rowtype6
            r[2+offside] += rowtype1
            r[3+offside] += rowtype7
            r[4+offside] += rowtype1
            for l in range(0+offside):
                r[l] += " "*4
            for l in range(size-4-offside-1):
                r[l+4+offside+1]+=" "*4
        if numbers[i]=="3":
            r[0+offside] += rowtype1
            r[1+offside] += rowtype6
            r[2+offside] += rowtype1
            r[3+offside] += rowtype6
            r[4+offside] += rowtype1
            for l in range(0+offside):
                r[l] += " "*4
            for l in range(size-4-offside-1):
                r[l+4+offside+1]+=" "*4
        if numbers[i]=="4":
            r[0+offside] += rowtype3
            r[1+offside] += rowtype2
            r[2+offside] += rowtype1
            r[3+offside] += rowtype6
            r[4+offside] += rowtype9
            for l in range(0+offside):
                r[l] += " "*4
            for l in range(size-4-offside-1):
                r[l+4+offside+1]+=" "*4
        if numbers[i]=="5":
            r[0+offside] += rowtype1
            r[1+offside] += rowtype7
            r[2+offside] += rowtype1
            r[3+offside] += rowtype6
            r[4+offside] += rowtype1
            for l in range(0+offside):
                r[l] += " "*4
            for l in range(size-4-offside-1):
                r[l+4+offside+1]+=" "*4
        if numbers[i]=="6":
            r[0+offside] += rowtype8
            r[1+offside] += rowtype7
            r[2+offside] += rowtype1
            r[3+offside] += rowtype2
            r[4+offside] += rowtype1
            for l in range(0+offside):
                r[l] += " "*4
            for l in range(size-4-offside-1):
                r[l+4+offside+1]+=" "*4
        if numbers[i]=="7":
            r[0+offside] += rowtype1
            r[1+offside] += rowtype6
            r[2+offside] += rowtype9
            r[3+offside] += rowtype6
            r[4+offside] += rowtype9
            for l in range(0+offside):
                r[l] += " "*4
            for l in range(size-4-offside-1):
                r[l+4+offside+1]+=" "*4
        if numbers[i]=="8":
            r[0+offside] += rowtype1
            r[1+offside] += rowtype2
            r[2+offside] += rowtype1
            r[3+offside] += rowtype2
            r[4+offside] += rowtype1
            for l in range(0+offside):
                r[l] += " "*4
            for l in range(size-4-offside-1):
                r[l+4+offside+1]+=" "*4
        if numbers[i]=="9":
            r[0+offside] += rowtype1
            r[1+offside] += rowtype2
            r[2+offside] += rowtype1
            r[3+offside] += rowtype6
            r[4+offside] += rowtype9
            for l in range(0+offside):
                r[l] += " "*4
            for l in range(size-4-offside-1):
                r[l+4+offside+1]+=" "*4
        if (2 * i + 2)<len(num):
            for j in range(len(r)):
                r[j]+=" "*int(num[2*i+2])
    emoji = ""
    for m in range(size-1):
        emoji += r[m]+"\n"
    emoji += r[size-1]
    #emoji = r[0]+"\n"+r[1]+"\n"+r[2]+"\n"+r[3]+"\n"+r[4]+"\n"+r[5]+"\n"+r[6]

    return (emoji)


num = input("please input the number to be print ")
print(numberC("8739542740987654321,0,4,1,3,2,4,1,4,2,3,1,5,2,4,3,4,5,6,3,1,2,3,1,2,3,5,1,5,4,1,6,2,5,1,3,2,1"))