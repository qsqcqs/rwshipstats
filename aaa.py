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
sw=[0,0,0,0,0,0,0,0,0,0]
sl=[0,0,0,0,0,0,0,0,0,0]
for w in pss:
    sw[int((w[0])[0])]=sw[int((w[0])[0])]+1
    sw[int((w[0])[2])]=sw[int((w[0])[2])]+1
    sl[int((w[1])[0])]=sl[int((w[1])[0])]+1
    sl[int((w[1])[2])]=sl[int((w[1])[2])]+1
print(sw)
print(sl)
sr=[0,0,0,0,0,0,0,0,0,0]
x=0
while x<10:
    sr[x]=f"{100*sw[x]/(sl[x]+sw[x])}%"
    x=x+1
print(sr)