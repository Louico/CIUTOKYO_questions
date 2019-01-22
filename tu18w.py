import random
def bin_random():
    ran = random.random()
    if ran<0.5:
        return False
    if ran>0.5:
        return True
data_path = "./tu18w_data/"
prog5 = data_path+"prog5.txt"
prog6 = data_path+"prog6.txt"
prog7 = data_path+"prog7.txt"
def find_s_t(row):
    i = 0
    s = 0
    t = 0
    lst=[]
    while i < len(row):
        char = row[i]
        print("this char is ",char,"s = %r, t = %r"%(s,t),"i = ",i)
        if char =="c":
            lst.append(row[i+1:i+5])
            i = int(row[i+1:i+5])-1
        if char =="r":
            if len(lst):
                i = int(lst.pop(-1))-1
            else:
                i+=1
        if char =="S":
            s += 1
            i += 1
        if char == "s":
            s -= 1
            i += 1
        if char == "T":
            t += 1
            i += 1
        if char == "t":
            t -= 1
            i += 1
        if char == "f":
            break
        if char == "j":
            num = int(row[i+1:i+5])
            i = num-1
            print("j jump to ",i,"is ",row[i])
        if char == "b":
            if s>0:
                num = int(row[i+1:i+5])
                i = num-1
                print("b jump to ",i,"is ",row[i])
            else:
                i += 5




    return s,t
#print(find_s_t("SSSSj0013ssTb0010f"))
#print(find_s_t("TSSSSb0012fssTTj0006"))
#print(find_s_t("j0018j0013Tfj0011j0006"))
#print(find_s_t("c0007fSSttr"))
#print(find_s_t("c0007fSSttr"))
#print(find_s_t("Tc0008fTc0015rsr"))
def find_s_t_v2(row):
    i = 0
    lst=[]
    k = 0
    counter = [0]*len(row)
    while i < len(row):
        if k % 10000000==0:
            number = 0
            for i in counter:
                if i==0:
                    number+=1
            #print("number is ", number)

        k+=1
        counter[i]+=1
        char = row[i]
        #print("this char is ",char,"s = %r, t = %r"%(s,t),"i = ",i)
        if char =="c":
            lst.append(row[i+1:i+5])
            i = int(row[i+1:i+5])-1
        if char =="r":
            if len(lst):
                i = int(lst.pop(-1))-1
            else:
                i+=1
        if char =="S":
            i += 1
        if char == "s":
            i += 1
        if char == "T":
            i += 1
        if char == "t":
            i += 1
        if char == "f":
            break
        if char == "j":
            num = int(row[i+1:i+5])
            i = num-1
            #print("j jump to ",i,"is ",row[i])
        if char == "b":
            if bin_random():
                num = int(row[i+1:i+5])
                i = num-1
                #print("b jump to ",i,"is ",row[i])
            else:
                i += 5



    return number,counter
with open(prog5) as f:
    text = f.read()
print(len(text))
time = len(text)
for i in range(20):

    times,_ = find_s_t_v2(text)
    if times < time:
        time = times
    print("the ",i," time of exp: ",time)
#print(find_s_t("TSSSSb0012fssTTj0006"))