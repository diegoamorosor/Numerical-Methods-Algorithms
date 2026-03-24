import sympy
def f(x1,fun):
    x=sympy.symbols('x')
    valor=float(sympy.sympify(fun).subs(x,x1))
    return(valor)

def simpson(a, b, n,fun ):

    h = (float(b - a) / n)
    print("El valor de h  es: ",h)
    sum = f(a,fun) + f(b,fun);

    for i in range(1, n ):
        if (i % 3 == 0):
            sum = sum + 2 * f((a + i * h),fun)
        else:
            sum = sum + 3 * f((a + i * h),fun)

    return ((( 3 * h) / 8 ) * sum )

print("Datos raiz cuadrada=sqrt(x) seno=sin(x) coseno=cos(x) tangente=tan() exponente=x**(valorExponente)")
print("Ingrese la funcion:")
funcion=input()
print("Ingrese limite inferior: ")
a = float(input())
print("Ingrese limite superior: ")
b = float(input())
print("Ingrese el numero de segmentos: ")
n = int((input()))


resultado = simpson(a,b,n,funcion)

print("El resultado de la integral aproximada es :", resultado)
