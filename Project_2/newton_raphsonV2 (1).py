import numpy as np
import matplotlib as plt
import math

def functions(xk,yk,zk):

    F = 3*xk - math.cos(yk*zk)-0.5
    G = xk**2 -(81*(yk+0.1)**2)+math.sin(zk)+1.06
    H = math.e **-xk*yk= 20*zk + (10*math.pi -3)/(3)

    F = np.array(
            [F,G,H])
            

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

def initial_point():
    I = np.array([0.1,0.1,-0.1])
    return I



def newton_raphson(functions, jacobian, initial_point, tol=1e-8, max_iter=100):
    I = initial_point()
    xk = I[0,0]
    yk = I[0,1]
    zk = I[0,2]
    iterations = 0
    while iterations <= max_iter:
        J = jacobian(np.array([xk, yk, zk]))
        F = functions(np.array([xk, yk, zk]))

        point = I - J.inverse() * F
        if(point[0,0] < tol and point[0,1] <tol and point[0,2]<tol):
            max_abs_value = float(functions(point))
            return point, iterations, max_abs_value
        else:
            xk = point[0,0]
            yk = point[0,1]
            zk = point[0,2]
            print("iteration "+ str(iterations)+ str(point)+ "\n")


    

    #f_par = ((3*x) - math.cos(y*z) - (1/2)) + (fx) * (x-xk) + (fy) * (y-yk) + fz * (z-zk)
    #g_par = ((x**2) - 81*(y+0.1)**2 + math.sin(z) + 1.06) + gx * (x-xk) + gy * (y-yk) + gz * (z-zk)
    #h_par = (math.e**(-(x*y)) + 20*z + ((10 * math.pi) - 3)/3) + hx * (x-xk) + hy * (y-yk) + hz * (z-zk)
    
   

    

    return point, iterations, max_abs_value

def main():
    pass
    

