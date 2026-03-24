import sympy
def f(x1,fun):
    x=sympy.symbols('x')
    valor=float(sympy.sympify(fun).subs(x,x1))
    return(valor)

def bisec1 (funcion,xl,xr,xu,es,ea,cont):
    na=0
    iter=0;
    while ea>=es :
        xrold=xr
        xr=(xl+xu)/2
        limInY=f(xl,funcion)
        limSupY=f(xu,funcion)
        pntm=f(xr,funcion)
        if iter==0:
            ea=1
        else:
            ea=abs((xr-xrold)/xr)*100
        if limInY * pntm<0:
            xu=xr
        elif limInY*pntm > 0:
            xl=xr
        else:
            ea=0
        iter=iter+1

    print("Nro.Iteraciones:",iter,"  Raiz ",cont,": ",xr,"   Ea%: ",ea,"   Es%",es)

cont=1
print("Datos raiz cuadrada=sqrt(x) seno=sin(x) coseno=cos(x) tangente=tan() exponente=x**(valorExponente)")
print("Ingrese la funcion:")
funcion=input()
print("Ingrese Intervalos [a,b]")
a=float(input("Ingresa a: "))
b=float(input("Ingresa b: "))
div=float(input("Ingrese Numero de divisiones: "))
dX=((b-a)/div)
es=0
print("Desea ingresar el error en % o el numero de cifras? e/c e=error c=numero cifras")
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
    cont=cont+1
    valorYA=f(res,funcion)
    if cont==0:
        valorYV=valorYA
        resXV=res
        res=res+dX
        cont=cont+1
    else:

        if(valorYV*valorYA<0):
            bisec1(funcion,resXV,((resXV+res)/2),res,es,1,nR)
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
