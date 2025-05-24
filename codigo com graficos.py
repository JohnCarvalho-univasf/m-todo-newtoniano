import math as m 
import sympy as sym 
from sympy.plotting import*
x = sym.symbols("x")
função = x**2 - 2
plot(função,(x,-2,2))

def f(x):
    f=x**2-2
    return f

def f1(x):
    f1 = 2*x
    return f1
def newton(f,f1,x,tol,ite_max):
    aux = 0
    while aux <= ite_max:
        x = x - f(x)/f1(x)
        print(x)
        aux += 1
        if abs(f(x)) < tol:
            return"a raiz aproximada é:  ",x
            return "o metodo falhou após", aux,"interações"
 
            
        