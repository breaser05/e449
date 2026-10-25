import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd


df = pd.read_csv('E449_Project2_oring_data.csv')


def functions(r,choice):
    if choice == 3:
        xk, yk, zk = r
        F = 3*xk - math.cos(yk*zk)-0.5
        G = xk**2 -(81*(yk+0.1)**2)+math.sin(zk)+1.06
        H = math.exp(-xk*yk)+ 20*zk + (10*math.pi -3)/(3)

        F = np.array(
                [F,G,H])
        return F
    elif choice == 2:
        a = r[0]
        b = r[1]
        p = np.zeros(23)
        for i in range(23):
            t = df['temp_f'][i]                    
            p[i] = 1/(1+np.exp(-(a+b*t)))
        F = 0
        G = 0
        for i in range(23):
            y = df['distress'][i]
            t = df['temp_f'][i]
            F += y-p[i]
            G += t*(y-p[i])
            return np.array([F,G])
    else:
        raise ValueError("Invalid choice. Must be 2 or 3.")


    

def jacobians(r,choice):
    if choice == 3:
        xk, yk, zk = r

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
    if choice == 2:
        a = r[0]
        b = r[1]
        p = np.zeros(23)
        for i in range(23):
            t = df['temp_f'][i]
            p[i] = 1/(1+np.exp(-(a+b*t)))
        Fa=Fb=Ga=Gb = 0
        for i in range(23):
            t = df['temp_f'][i]

            
            Fa += -(p[i]*(1-p[i]))
            Fb += -(t * p[i] * (1-p[i]))
            
            Ga += -(t * p[i]*(1-p[i]))
            Gb += -((t ** 2)*p[i]*(1-p[i]))
            
        J = np.array([
            [Fa, Fb],
            [Ga, Gb]
        ])
        return J

    

def initial_point(choice):
    if choice == 3:
        return np.array([0.1,0.1,-0.1])
    elif choice == 2:
        return np.array([0,0])
    

def newton_raphson_2d(function, jacobian, initialpoint,tol=1e-8,max_iter=100):
    
    i = initial_point(2)
    a = i[0]
    b = i[1]
    iterations = 0
    point = [a,b]
    while iterations < max_iter:
            
            delta = np.linalg.solve(jacobian(point,2), -functions(point,2))
            point = point + delta
            iterations += 1
            max_abs_value = np.max(np.abs(functions(point,2)))
            if(max_abs_value < tol):
                break
            print(f"Iteration {iterations}\npoint = {point}\nmax_abs_value = {max_abs_value}\n")
    return point, iterations, max_abs_value


def newton_raphson(function, jacobian, initialPoint, tol=1e-8, max_iter=100):
    I = initialPoint
    xk = I[0]
    yk = I[1]
    zk = I[2]
    iterations = 0
    point = np.array([xk, yk, zk], dtype=float)
    iterations = 0
    max_abs_value = np.max(np.abs(functions(point,3)))
    while iterations < max_iter:
        
        delta = np.linalg.solve(jacobian(point,3), -functions(point,3))
        point = point + delta
        iterations += 1
        max_abs_value = np.max(np.abs(functions(point,3)))
        if(max_abs_value < tol):
            break
        print(f"Iteration {iterations}\npoint = {point}\nmax_abs_value = {max_abs_value}\n")
            
    return point, iterations, max_abs_value
        




    #f_par = ((3*x) - math.cos(y*z) - (1/2)) + (fx) * (x-xk) + (fy) * (y-yk) + fz * (z-zk)
    #g_par = ((x**2) - 81*(y+0.1)**2 + math.sin(z) + 1.06) + gx * (x-xk) + gy * (y-yk) + gz * (z-zk)
    #h_par = (math.e**(-(x*y)) + 20*z + ((10 * math.pi) - 3)/3) + hx * (x-xk) + hy * (y-yk) + hz * (z-zk)





def main():
    ip = initial_point(3)
    point, iterations, max_abs_value = newton_raphson(functions, jacobians, ip)
    print(f"\nfinal point = {point}\niterations = {iterations}\n final max_abs_value = {max_abs_value}")

    ip2 = initial_point(2)
    point2, iterations2, max_abs_value2 = newton_raphson_2d(functions, jacobians, ip2)


if __name__ == "__main__":
    main()