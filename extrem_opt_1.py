import matplotlib.pyplot as plt
import numpy as np
import random as rn
import math 
from sympy import symbols, Eq, solve

# Вариант 4

a = -1
b = 2
eps = 0.001

N = 1000

def f(x):
    return (x**2)/2 - np.sin(x)

def df(x):
    return 4*(x**3)-(4*x)

def mono_inter():
    x_sym = symbols('x')
    left_border  = -N
    right_border = 0
    equation = Eq(4*x_sym**3  - 4*x_sym, 0)
    roots = solve(equation, x_sym)
    inters = []
    for i in range(len(roots)):
        right_border = roots[i]
        sign = 1 if df((rn.uniform(left_border, right_border)))>=0 else -1 
        if(i==0):
            inters.append("Промежуток возрастания: [-∞:{}]".format(right_border) if (sign >= 0) else "Промежуток убывания: [-∞:{}]".format(right_border))
            left_border = right_border
            continue
        inters.append("Промежуток возрастания: [{}:{}]".format(left_border, right_border) if (sign >= 0) else "Промежуток убывания: [{}:{}]".format(left_border, right_border))
        left_border = right_border
        if(i==len(roots)-1):
            sign = 1 if df((rn.uniform(left_border, right_border)))>=0 else -1 
            inters.append("Промежуток возрастания: [{}:∞]".format(left_border) if (sign >= 0) else "Промежуток убывания: [{}:∞]".format(left_border))
    return inters       


x_data = np.linspace(a,b,N,float)
y_data = f(x_data)

def gold(a, b, eps):
    n = 0
    print("Метод Золотого сечения")
    g = (math.sqrt(5) - 1.0) / 2
    k = 0
    a1 = a + (1 - g) * (b - a)
    b1 = a + g * (b - a)
    while abs(b - a) > eps:
        n+=1 
        if f(a1) > f(b1):
            a = a1
            a1 = b1
            b1 = a + g * (b - a)
        else:
            b = b1
            b1 = a1
            a1 = a + (1 - g) * (b - a)
        if ++k > eps:
            break
    min = (a + b) / 2
    print("Итераций:", n)
    return min
x_data = np.linspace(a,b,N,float)
y_data = f(x_data)

delta = eps

print("№1:")
print(mono_inter())

print("№2:")
gold_answ  = gold(a,b,eps) 

print("Найденный минимум по Золотому сечению:", gold_answ)
print("Значение функции в точке:", f(gold_answ))
plt.plot(x_data, y_data)
plt.show()