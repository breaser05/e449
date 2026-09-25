import numpy as np
import matplotlib as plt
import math



def newton_raphson(functions, jacobian, initial_point, tol=1E-8, max_iter=100):
    xk = 0.1
    yk = 0.1
    zk = -0.1

    k = 0
    
    gx = 2 * xk
    gy = -162 * yk - 16.2
    gz = math.cos(zk)
    
    fx = 3
    fy = 9 + zk * math.sin(yk* zk)
    fz = yk * math.sin(yk*zk)
    
    hx = -yk * math.e**(xk*yk)
    hy = -xk * math.e**-(xk*yk)
    hz = 20
    
    f_par = ((3*x) - math.cos(y*z) - (1/2)) + (fx) * (x-xk) + (fy) * (y-yk) + fz * (z-zk) 
    g_par = ((x**2) - 81*(y+0.1)**2 + math.sin(z) + 1.06) + gx * (x-xk) + gy * (y-yk) + gz * (z-zk)
    h_par = (math.e**(-(x*y)) + 20*z + ((10 * math.pi) - 3)/3) + hx * (x-xk) + hy * (y-yk) + hz * (z-zk)
    
    np.arrar
    
    