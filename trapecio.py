import sympy
def f(x1,fun):
    x=sympy.symbols('x')
    valor=float(sympy.sympify(fun).subs(x,x1))
    return(valor)

def trapezoidal (a, b, n,fun):

    h = (b - a) / n
    print("El valor de h  es: ",h)
    s = (f(a,fun) + f(b,fun))

    i = 1
    while i < n:
        s += 2 * f((a + i * h),fun)
        i += 1
    return ((h / 2) * s)


print("Datos raiz cuadrada=sqrt(x) seno=sin(x) coseno=cos(x) tangente=tan() exponente=x**(valorExponente)")
print("Ingrese la funcion:")
funcion=input()
print("Ingrese limite inferior: ")
a = float(input())
print("Ingrese limite superior: ")
b = float(input())
print("Ingrese el numero de segmentos: ")
n = int((input()))
vA=trapezoidal(a,b, n,funcion)
print ("El valor aproximado de la integral por debajo de la curva  es: ",vA)
