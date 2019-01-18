path = "./programtest.txt"

def read_program(path):
    with open(path) as f:
        program = f.read()
    program = program.split("\n")
    row = len(program)
    return program,row
def find_char(text,char):
    num = 0
    for i in text :
        for j in i:
            if j == char:
                num+=1
    return num
program,row = read_program(path)
print(find_char(program,";"))
