M = 100
txt_path = "./data/mat1.txt"
MAT1 = []
with open(txt_path) as f:
    mat = f.read()
    #print(mat)
    mat = mat.split(".")[0]
    #print(mat)
    mat1 = mat.split(",")
    #print(mat1)
    #print(len(mat1))
    #print(len(mat1[0].split()))

    for i in mat1:
        MAT1.append(i.split())

print(MAT1)
txt_path = "./data/mat2.txt"
MAT2 = []
with open(txt_path) as f:
    mat = f.read()
    #print(mat)
    mat = mat.split(".")[0]
    #print(mat)
    mat2 = mat.split(",")
    #print(mat2)
    #print(len(mat2))
    #print(len(mat2[0].split()))

    for i in mat2:
        MAT2.append(i.split())
print(MAT2)
#print(MAT1)
#print(mat1)
d = 0

m=[]
print(len(MAT1))
print(len(MAT1[1]))
print(len(MAT2))
print(len(MAT2[1]))
for i in range(len(MAT1)):
    a = []
    for j in range(len(MAT2[0])):
        d = 0
        for k in range(len(MAT1[i])):
            d+= float(MAT1[i][k])*float(MAT2[k][j])
        a.append(d)
    m.append(a)

print(m)
print(len(m))
print(len(m[1]))

trace = 0

for i in range(min(len(m),len(m[0]))):
    trace += float(m[i][i])
print(trace)




def compute(iindex, jindex, whicharray, cachesize, sflag, storediindex, storedjindex,stime):
    #cache age grow
    for l in range(cachesize):
        stime[l]+=1
    #cache hit
    for l in range(cachesize):
        if(sflag[l]==whicharray and storediindex[l] == iindex and storedjindex[l] == jindex):
            stime[l]=0
            print("hit")
            return 0
    #not hit and empty page exist
    for l in range(cachesize):
        if sflag[l] == -1 :
            sflag[l] = whicharray
            storediindex[l] = iindex
            storedjindex[l] = jindex
            stime[l] = 0
            print("not hit and put in empty page")
            return 1
    #not hit and no empty space
    max = 0
    for l in range(cachesize):
        if stime[l]>stime[max]:
            max = l
    #set new data to LRU
    stime[max] = 0
    sflag[max] = whicharray
    storediindex[max] = iindex;
    storedjindex[max] = jindex;
    #print("not hit and put in LRU")
    return 1

cachesize = 50;
sflag = [-1]*cachesize
stime = [M]*cachesize
si = [-1]*cachesize
sj = [-1]*cachesize
m=5
n=10
time = 0
times = 0
i = 0
while i<m:
    j = 0
    while j < m:
        k = 0
        while k < n:
            time = time +compute(i ,k, 1, cachesize, sflag, si,sj,stime)+compute(k,j,2,cachesize,sflag,si,sj,stime)
            times = times +2
            #for q in range(cachesize):
            k = k+1
        j = j+1
    i = i+1

print("without LRU cache: ",time)
print("with LRU cache: ",times)






#cache hit

