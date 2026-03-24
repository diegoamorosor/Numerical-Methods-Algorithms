import math
import sympy
def f(x1,fun):
    x=sympy.symbols('x')
    valor=float(sympy.sympify(fun).subs(x,x1))
    return(valor)

def F(x,funcion):
    return f(x,funcion)+x

def abierto(funcion,x0,es,iter,ea,cont):
        xr=x0
        iter=0
        while ea>=es:
            xrold=xr
            xr=F(xrold,funcion)
            iter=iter+1
            if xr!=0:
                ea=abs((xr-xrold)/xr)*100

        print("Raiz ",cont,":",xr,"   Ea%:","%.4f" %ea," Es%:",es)




def abierto2(funcion,a,b,es,imax,iter,ea,cont):
    xa=("%.2f" %a)
    xb=("%.2f" %b)
    a=float(xa)
    b=float(xb)
    xo=(a+b)/2
    print("Valor xo= ",xo)

    print(a,b)
    iter=0
    xr=xo
    while ea>=es:
        xrold=xr
        xr=F(xrold,funcion)
        iter=iter+1
        if xr!=0:
            ea=abs((xr-xrold)/xr)*100

    print("Raiz ",cont,":",xr,"   Ea%:","%.6f" %ea,"  Es",es)

print("Datos raiz cuadrada=sqrt(x) seno=sin(x) coseno=cos(x) tangente=tan() exponente=x**(valorExponente)")
print("Ingrese la funcion:")
funcion=input()
print("Desea ingresar un valor  inicial?S/N ")
x=input()
if x=="S":
    print("Ingrese xo:")
    xo=float(input())
    print("Desea ingresar el error o el numero de cifras? e/c e=error c=numero cifras")
    opc=input()
    if(opc=="e" or opc=="E" ):
        print("Ingrese es:")
        es=float(input())
        abierto(funcion,xo,es,0,1,1)
    else:
        numCifras=float(input("Ingrese el Numero de cifras: "))
        es=0.5*10**(2-numCifras)
        abierto(funcion,xo,es,0,1,1)

else:
    print("Ingrese Intervalos [a,b]")
    a=float(input("Ingresa a: "))
    b=float(input("Ingresa b: "))
    div=float(input("Ingrese Numero de divisiones: "))
    dX=((b-a)/div)
    print(dX)
    es=0
    print("Desea ingresar el error o el numero de cifras? e/c e=error c=numero cifras")
    opc=input()
    if(opc=="e" or opc=="E" ):
        print("Ingrese es:")
        es=float(input())
    else:
        numCifras=float(input("Ingrese el Numero de cifras: "))
        es=0.5*10**(2-numCifras)
    res=a
    valorYV=0
    valorYA=0
    cont=0
    nR=1
    while res<=b:

        valorYA=f(res,funcion)
        if cont==0:
            valorYV=valorYA
            resXV=res
            res=res+dX

            cont=cont+1
        else:

            if(valorYV*valorYA<0):
                abierto2(funcion,resXV,res,es,0,0,1,nR)
                nR=nR+1
                valorYV=valorYA
                resXV=res
                res=res+dX
                cont=cont+1
            else:
                valorYV=valorYA
                resXV=res
                res=res+dX

                cont=cont+1
