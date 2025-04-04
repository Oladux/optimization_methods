import sympy
import numpy as np
def func(x1,x2):
   return (x1**2-x2+1)**2 + x2

eps = 0.01
N = int(1/eps)

choise = int(input('Метод: \n 1: Перебора 2: Гаусса \n'))

borders_x1 = [-2., 2.]
borders_x2 = [-3., 3.]

if(choise==1):
    ax, bx = borders_x1[0], borders_x1[1] 
    ay, by = borders_x2[0], borders_x2[1] 
    min = 10000000
    func_val = 0
    xi = [0, 0]

    for i in range(N):
        xi[0] = ax + i * ((bx - ax)/N)
        for j in range(N):
            xi[1] = ay + j * ((by - ay)/N)
            func_val = func(xi[0],xi[1])
            if (func_val <= min):
                min_points = [xi[0],xi[1]]
                min = func_val

    print(min_points[0],min_points[1])
    print(min)
    
if(choise==2):
    start_point = np.array([[0], [0]])
    x_matrix = np.array(start_point)
    x1, x2 = sympy.symbols('x1 x2')
    dx1 = sympy.diff((x1**2-x2+1)**2 + x2, x1)
    dx2 = sympy.diff((x1**2-x2+1)**2 + x2, x2)   
    second_diff_eq = []
    n = 0
    while n<N:
        d2x1 = sympy.diff(dx1, x1)
        d2x2 = sympy.diff(dx2, x2)
        d1d2x = sympy.diff(dx1, x2)
        d2d1x = sympy.diff(dx2, x1)

        for eq in [d2x1,d2x2,d1d2x,d2d1x]:
            second_diff_eq.append(eq.subs({x1:x_matrix[0][0], x2:x_matrix[1][0]}))

        grad = np.array([[dx1.subs({x1:x_matrix[0][0], x2:x_matrix[1][0]})],[dx2.subs({x1:x_matrix[0][0],x2:x_matrix[1][0]})]])
        gesse_matrix = np.astype(np.array([[second_diff_eq[0],second_diff_eq[2]],[second_diff_eq[3],second_diff_eq[1]]]), np.float32)
        inv_gesse_matrix = np.linalg.inv(gesse_matrix)

        delta = np.matmul(inv_gesse_matrix, grad) * (-1)
        x_matrix = np.add(x_matrix, delta)
        n+=1
        if(abs((grad[1]+grad[0])) < eps):
            print(x_matrix)
            print(func(x_matrix[0][0],x_matrix[1][0]))
            break