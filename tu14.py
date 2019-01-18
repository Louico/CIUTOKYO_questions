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
    pass
text,program,row = read_program(path)
print(find_char(program,";"))
#print(find_str(program,"main"))