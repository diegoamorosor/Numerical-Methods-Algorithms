import numpy as np
def seidel(a, x ,b):
    n = len(a)
    for j in range(0, n):
        d = b[j]
        for i in range(0, n):
            if(j != i):
                d-=a[j][i] * x[i]
        x[j] = d / a[j][j]
    return x

n = int(input("Ingrese numero de variables ? "))
a = np.zeros(shape=(n,n))
b = np.zeros(shape=(n))

for i in range(0,n):
    print("Ingrese los valores de la ",(i+1)," fila:")
    for j in range(0,n):
        print("Ingrese x",(j+1),":")
        a[i][j]=float(input())
    print("Ingrese b",(i+1),":")
    b[i]=float(input())

es=0
print("Desea ingresar el error o el numero de cifras? e/c e=error c=numero cifras")
opc=input()
if(opc=="e" or opc=="E" ):
    print("Ingrese es:")
    es=float(input())
else:
    numCifras=float(input("Ingrese el Numero de cifras: "))
    es=0.5*10**(2-numCifras)

print("Ingrese nro de iteraciones maximas? ")
itmax=int(input())
x=np.zeros(shape=(n))
oldx=np.zeros(shape=(n))
ea=np.zeros(shape=(n))
cent=-1;
cont=1;
while (cent==-1):
    for j in range(0, n):
        oldx[j]=x[j]
    x=seidel(a, x, b)
    for k in range(0,n):
        if(x[k]!=0):
            ea[k]=abs(((x[k]-oldx[k])/x[k])*100)
    for j in range(0, n):
        if (ea[j]<es):
            cent=0
        else:
            cent=-1
            break;
    if (cont>itmax):
        break;
    cont=cont+1


for i in range(0,n):
    print("x",i+1,": ",x[i],"  ea%: ",ea[i],"  es%:",es)
