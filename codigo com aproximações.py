import math as m 
import sympy as sym 
from sympy.plotting import*

def raiz_quadrada_de_2_newton(x0=1.0, tolerancia=1e-10, max_iter=4):
    x = x0
    for i in range(max_iter):
        fx = x**2 - 2
        dfx = 2 * x
        x_novo = x - fx / dfx

        print(f"Iteração {i+1}: x = {x_novo}")

        if abs(x_novo - x) < tolerancia:
            break
        x = x_novo

    return x_novo
# Executar
resultado = raiz_quadrada_de_2_newton()
print(f"\nAproximação final de √2: {resultado}")


