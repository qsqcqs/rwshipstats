a=(open("/home/qsqcqs/indres.txt", "r").read())

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
print(pss)

x=0
thrsc=[]
while x<10:
    y=x+1
    while y<10:
        z=y+1
        while z<10:
            t=0
            s=1
            
#           xy score
            k=0
            while k < len(pss):
                
                if (pss[k][0]).find(f"{x}x{y}") != -1:
                    t=t+1
                    s=s*int(pss[k][1])
                
                #yz score
                if (pss[k][0]).find(f"{y}x{z}") != -1:
                    t=t+1
                    s=s*int(pss[k][1])
                
                #xz score
                if (pss[k][0]).find(f"{x}x{z}") != -1:
                    t=t+1
                    s=s*int(pss[k][1])
                
                k=k+1   
            print(s)
            print(t)
            if t != 0:
                no=0
                if x == 1:
                    if y == 2:
                        no=1
                    if z == 2:
                        no=1
                if y == 1:
                    if x == 2:
                        no=1
                    if z == 2:
                        no=1
                if z == 1:
                    if x == 2:
                        no=1
                    if y == 2:
                        no=1
                if no==0:
                    thrsc.append([f"{x}x{y}x{z}",s**(1/t)])
            print(f"{x},{y},{z}")
            z=z+1
        
        y=y+1    
            
    x=x+1
k=0
while k<3:
    n=0
    while (n+1)<len(thrsc):
        if thrsc[n][1]<thrsc[n+1][1]:
            a=thrsc[n]
            thrsc[n]=thrsc[n+1]
            thrsc[n+1]=a
            k=0
        n=n+1
    k=k+1

print(thrsc)
