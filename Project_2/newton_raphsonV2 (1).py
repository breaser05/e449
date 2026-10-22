import numpy as np
import matplotlib.pyplot as plt
import math

def functions(p):
    xk, yk, zk = p
    F = 3*xk - math.cos(yk*zk)-0.5
    G = xk**2 -(81*(yk+0.1)**2)+math.sin(zk)+1.06
    H = math.exp(-xk*yk)+ 20*zk + (10*math.pi -3)/(3)

    F = np.array(
            [F,G,H])


    return F

def jacobians(p):
    xk, yk, zk = p

    gx = 2 * xk
    gy = -162 * yk - 16.2
    gz = math.cos(zk)

    fx = 3
    fy = zk * math.sin(yk* zk)
    fz = yk * math.sin(yk*zk)

    hx = -yk * math.exp(-xk*yk)
    hy = -xk * math.exp(-xk*yk)
    hz = 20

    J = np.array([
        [fx, fy, fz],
        [gx, gy, gz],
        [hx, hy, hz]
    ])

    return J

def initial_point():
    return np.array([0.1,0.1,-0.1])
    



def newton_raphson(function, jacobian, initialPoint, tol=1e-8, max_iter=100):
    I = initialPoint
    xk = I[0]
    yk = I[1]
    zk = I[2]
    iterations = 0
    point = np.array([xk, yk, zk], dtype=float)
    iterations = 0
    max_abs_value = np.max(np.abs(functions(point)))
    while iterations < max_iter:
        
        delta = np.linalg.solve(jacobian(point), -functions(point))
        point = point + delta
        iterations += 1
        max_abs_value = np.max(np.abs(functions(point)))
        if(max_abs_value < tol):
            break
        print(f"Iteration {iterations}\npoint = {point}\nmax_abs_value = {max_abs_value}\n")
            
    return point, iterations, max_abs_value
        




    #f_par = ((3*x) - math.cos(y*z) - (1/2)) + (fx) * (x-xk) + (fy) * (y-yk) + fz * (z-zk)
    #g_par = ((x**2) - 81*(y+0.1)**2 + math.sin(z) + 1.06) + gx * (x-xk) + gy * (y-yk) + gz * (z-zk)
    #h_par = (math.e**(-(x*y)) + 20*z + ((10 * math.pi) - 3)/3) + hx * (x-xk) + hy * (y-yk) + hz * (z-zk)





def main():
    ip = initial_point()
    point, iterations, max_abs_value = newton_raphson(functions, jacobians, ip)
    print(f"\nfinal point = {point}\niterations = {iterations}\n final max_abs_value = {max_abs_value}")


if __name__ == "__main__":
    main()
