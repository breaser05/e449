import numpy as np
import matplotlib as plt
import math

def functions(xk,yk,zk):
    F = np.array()
    return F

def jacobian(xk,yk,zk):
    gx = 2 * xk
    gy = -162 * yk - 16.2
    gz = math.cos(zk)
       
    fx = 3
    fy = 9 + zk * math.sin(yk* zk)
    fz = yk * math.sin(yk*zk)
       
    hx = -yk * math.e**(xk*yk)
    hy = -xk * math.e**-(xk*yk)
    hz = 20

    J = np.array([
        [fx, fy, fz],
        [gx, gy, gz],
        [hx, hy, hz]
    ])

    return J


def newton_raphson(functions, jacobian, initial_point, tol=1e-8, max_iter=100):
   
    xk, yk, zk = initial_point

    k = 0
    
    f_par = ((3*x) - math.cos(y*z) - (1/2)) + (fx) * (x-xk) + (fy) * (y-yk) + fz * (z-zk) 
    g_par = ((x**2) - 81*(y+0.1)**2 + math.sin(z) + 1.06) + gx * (x-xk) + gy * (y-yk) + gz * (z-zk)
    h_par = (math.e**(-(x*y)) + 20*z + ((10 * math.pi) - 3)/3) + hx * (x-xk) + hy * (y-yk) + hz * (z-zk)
    
   
    jacobian(np.array([xk, yk, zk]))

    np.linalg.solve(J,F)

    return point, iterations, max_abs_value

initial_point = np.array([0.1, 0.1, -0.1])