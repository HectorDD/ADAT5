from sys import stdin
#Héctor David Delgado
#Cod: 0217014
# def initpaint(n,m):
#     mypaint=[]
#     for i in range(n):
#         l=[]
#         for j in range(m):
#             l.append(0)
#         mypaint.append(l)
#     return mypaint
def imprimirpint(paint):
    for i in paint:
        print (i)
def paintzone(mypaint,r,c,i,j,n,m):
    cont1=i    
    while i+r<=n and cont1<=(i+r)-1:
        cont2=j
        while j+c<=m and cont2<=(j+c)-1:
            if mypaint[cont1][cont2]==1:
                mypaint[cont1][cont2]=0                
            else:
                #print("x es : ",cont1," y es : ",cont2)
                mypaint[cont1][cont2]=1
            cont2+=1
        cont1+=1
    return mypaint
def solve(n,m,r,c,paint,mypaint):
    cantidad=0
    for i in range(n):
        for j in range(m):
            if paint[i][j]!=mypaint[i][j] and i+r<=n and j+c<=m:
                mypaint=paintzone(mypaint,r,c,i,j,n,m)
                cantidad+=1
            elif paint[i][j]!=mypaint[i][j]: #and (i+r>n+1 or j+c>m+1):
                #imprimirpint(mypaint)
                return -1
    #imprimirpint(mypaint)
    return cantidad 
def main ():
    line = stdin.readline()
    b = line.split()
    while b[0]!='0' and b[1]!='0'and b[2]!='0' and b[3]!='0':
        n=int(b[0])
        m=int(b[1])
        c=int(b[2])
        #print ("el c es: ", c)
        r=int(b[3])
        #print ("el r es: ", r)
        paint=[]
        mypaint=[]
        for j in range(n):
            l=[]
            l1 = stdin.readline() 
            l1=l1[:-1]
            lisnum=[]
            for t in l1:
                lisnum.append(int(t))
                l.append(0)
            paint.append(lisnum)
            mypaint.append(l)
        #imprimirpint(paint)
        print(solve(n,m,c,r,paint,mypaint))
        line = stdin.readline() 
        b = line.split()              
main()