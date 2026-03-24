from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def jacobi(A,b,N=25,x=None):
    if x is None:
        x = zeros(len(A[0]))

    D = diag(A)
    R = A - diagflat(D)

    for i in range(N):
        x = (b - dot(R,x)) / D
    return x

A = array([[6,1,1],[1,6,1],[1,2,-6]])
b = array([9,15,-3])
guess = array([2,0.5,20])

sol = jacobi(A,b,N=25,x=guess)

print("A:")
print(A)

print("b:")
print(b)

print("x:")
print(sol)
