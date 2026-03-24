import sympy
def f(x1,fun):
    x=sympy.symbols('x')
    valor=float(sympy.sympify(fun).subs(x,x1))
    return(valor)

def simpsons( a, b, n ,funct):
    h = ( b - a )/n
    print("El valor de h  es: ",h)
    x = list()
    fx = list()
    i = 0
    while i<= n:
        x.append(a + i * h)
        fx.append(f(x[i],funct))
        i += 1
    res = 0
    i = 0
    while i<= n:
        if i == 0 or i == n:
            res+= fx[i]
        elif i % 2 != 0:
            res+= 4 * fx[i]
        else:
            res+= 2 * fx[i]
        i+= 1
    res = res * (h / 3)
    return res

print("Datos raiz cuadrada=sqrt(x) seno=sin(x) coseno=cos(x) tangente=tan() exponente=x**(valorExponente)")
print("Ingrese la funcion:")
funcion=input()
print("Ingrese limite inferior: ")
a = float(input())
print("Ingrese limite superior: ")
b = float(input())
print("Ingrese el numero de segmentos: ")
n = int((input()))

resbtado=simpsons(a,b, n,funcion)

print("El valor aproximado de la integral es : ",resbtado)
