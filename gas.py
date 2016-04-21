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



	

		




        
def main ():
    line = stdin.readline()
    b = line.split()
    while b[0]!='0' and b[1]!='0':
        L=int(b[0])
        #print("Largo del camino : ",b[0])
        #print("Número de gasolineras : ",b[1])
        gas=[[0,0] for i in range(int(b[1]))]
        for j in range(int(b[1])):
            l = stdin.readline()
            z = l.split() 
            gas[j][0]=int(z[0])-int(z[1])
            gas[j][1]=int(z[0])+int(z[1])
        gas.sort()
        print (gas)
        solve(L,gas)
        line = stdin.readline() 
        b = line.split()              
main()