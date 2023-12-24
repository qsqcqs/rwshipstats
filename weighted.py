a=(open("/home/qsqcqs/mdata.txt", "r").read())

#print(a)
k=(a.find("\n"))
lst=[]
while k != -1:
    
    #print(a[0:k])
    lst.append(a[0:k])
    a=a[k+1:]
    k=(a.find("\n"))
#print(lst)
pss=[]
for s in lst:
    tmp=[]
    mmm=s.find(" ")
    while len(s)>3:
        tmp.append(s[0:mmm+1])
        s=s[k+mmm+2:]
        mmm=s.find(" ")
        #print(s)
    tmp.append(s)
    pss.append(tmp)
    #print(tmp)
#print(pss)
smag=[0,0,0,0,0,0,0,0,0,0]
sm=[0,0,0,0,0,0,0,0,0,0]
for w in pss:
    sm[int((w[0])[0])]=sm[int((w[0])[0])]+1
    sm[int((w[0])[2])]=sm[int((w[0])[2])]+1
    sm[int((w[1])[0])]=sm[int((w[1])[0])]+1
    sm[int((w[1])[2])]=sm[int((w[1])[2])]+1
    
    smag[int((w[0])[0])]=smag[int((w[0])[0])]+int(w[2])
    smag[int((w[0])[2])]=smag[int((w[0])[2])]+int(w[2])
    smag[int((w[1])[0])]=smag[int((w[1])[0])]+int(w[3])
    smag[int((w[1])[0])]=smag[int((w[1])[0])]+int(w[3])
x=0
while x<10:
    smag[x]=smag[x]/sm[x]
    x=x+1
print(smag)