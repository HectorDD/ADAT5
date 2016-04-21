from sys import stdin
#Héctor David Delgado
#Cod: 0217014
sol=[]
def solve(L,gas):
    global sol
    if gas[0][0] >0:
        return -1
    else:
        tmp=gas[0]
        for i in gas:
            if i[0]>0:
                sol.append(tmp)
                break
            elif i[0]<=0 and i[1]>tmp[1]:
                tmp=i
        if len(sol)<1:
            sol.append(tmp)
        i=0
        while i < len(gas):
            if gas[i][0]<=sol[len(sol)-1][1] and gas[i][1]>tmp[1]:
                tmp=gas[i]
            elif gas[i][0]>sol[len(sol)-1][1]:
                if not(tmp==sol[len(sol)-1]):
                    sol.append(tmp)
                    i-=1
            if sol[len(sol)-1][1]>=L:
                break
            i+=1
        if not(tmp==sol[len(sol)-1]):
                    sol.append(tmp)        
        if sol[len(sol)-1][1]<L:
            return -1
        else:
            return len(gas)-len(sol)        
def main ():
    global sol
    line = stdin.readline()
    b = line.split()
    while b[0]!='0' and b[1]!='0':
        L=int(b[0])
        gas=[[0,0] for i in range(int(b[1]))]
        for j in range(int(b[1])):
            l = stdin.readline()
            z = l.split() 
            gas[j][0]=int(z[0])-int(z[1])
            gas[j][1]=int(z[0])+int(z[1])
        gas.sort()
        sol=list()
        print(solve(L,gas))
        line = stdin.readline() 
        b = line.split()              
main()