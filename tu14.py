path = "./programtest.txt"

def read_program(path):
    with open(path) as f:
        program = f.read()
    programarray = program.split("\n")
    row = len(program)
    return program,programarray,row
def find_char(text,char):
    num = 0
    for i in text :
        for j in i:
            if j == char:
                num+=1
    return num
def find_str(text,str_to_find):
    result=[]

    for i in range(len(text)):
        if text[i].find(str_to_find)>0:
            #str1.find(str) return the position of str in str1
            tmp = str(i)+" "+text[i]
            result.append(tmp)
    return result

def find_duplicate(text):
    tmp=[]
    for i in range(len(text)-1):
        if text[i]==text[i+1]:
            tmp.append(text[i])
            #print("found same in row ",i)
    for j in range(len(tmp)-1):
        while (j+1<len(tmp) and tmp[j]==tmp[j+1]):
            del tmp[j]
    return tmp

def find_duplicate_V2(text):
    code={}

    tmp=[""]*len(text)
    for i in range(len(text)):
        text[i] = text[i].strip()
        code[text[i]] = code.get(text[i],[0,i])
        code[text[i]][0] += 1

            #print("found same in row ",i)
    #some effect to make dict ordered
    for k,v in code.items():
        if v[0]>1:
            tmp[v[1]]=k
    result = ""
    number = 0
    for i in tmp:
        if i:
            result+=i+"\n"
            number+=1

    return result[:-1],number

def find_similar_lines(text):
    pass
text,program,row = read_program(path)
#print(find_char(program,";"))
#print(find_str(program,"main"))
result,num = find_duplicate_V2(program)
print(num," duplicate lines \n",result)