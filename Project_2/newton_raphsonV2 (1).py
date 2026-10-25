# Henry Saam ,Laksh Solanki, Bryce Reaser
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd


#This is where the code gets the datapoints from the CSV file.
#this project uses Newton-Raphson to solve two systems of equations.
#It prints the results and plots the logistic regression curve.
df = pd.read_csv('E449_Project2_oring_data.csv')


def functions(r):
    if len(r) == 3:
# Gets the three unknown variables for Part I.
        xk, yk, zk = r
        F = 3*xk - math.cos(yk*zk)-0.5
        G = xk**2 -(81*(yk+0.1)**2)+math.sin(zk)+1.06
        H = math.exp(-xk*yk)+ 20*zk + (10*math.pi -3)/(3)
        F = np.array(
                [F,G,H])
        return F
# three nonlinear equations and return the three function values in an array
    elif len(r) == 2:
# gets alpha and beta
        a = r[0]
        b = r[1]
#calculate the probability
        p = np.zeros(23)
        for i in range(23):
            t = df['temp_f'][i]                    
            p[i] = 1/(1+np.exp(-(a+b*t)))
#Sets F and G to zero and calulates them
        F = 0
        G = 0
        for i in range(23):
            y = df['distress'][i]
            t = df['temp_f'][i]
            F += y-p[i]
            G += t*(y-p[i])
        return np.array([F,G])
#returns F and G in an array
    else:
        raise ValueError("Invalid choice. Must be 2 or 3.")


#jacobian function
def jacobians(r):
    if len(r) == 3:
        xk, yk, zk = r
#gets the X, Y and Z values.

#partial derivatives of G
        gx = 2 * xk
        gy = -162 * yk - 16.2
        gz = math.cos(zk)
#partial derivatives of F
        fx = 3
        fy = zk * math.sin(yk* zk)
        fz = yk * math.sin(yk*zk)
#partial derivatives of Z
        hx = -yk * math.exp(-xk*yk)
        hy = -xk * math.exp(-xk*yk)
        hz = 20
#puts the partials in an array and then return the array
        J = np.array([
            [fx, fy, fz],
            [gx, gy, gz],
            [hx, hy, hz]
        ])
        return J
    if len(r) == 2:
#Gets A and B 
        a = r[0]
        b = r[1]
#caluclates the probabilities
        p = np.zeros(23)
        for i in range(23):
            t = df['temp_f'][i]
            p[i] = 1/(1+np.exp(-(a+b*t)))
#sets the derivative to zero
        Fa=Fb=Ga=Gb = 0
#Calculate the four partial derivatives.
        for i in range(23):
            t = df['temp_f'][i]

            Fa += -(p[i]*(1-p[i]))
            Fb += -(t * p[i] * (1-p[i]))
            
            Ga += -(t * p[i]*(1-p[i]))
            Gb += -((t ** 2)*p[i]*(1-p[i]))
# Put the derivatives into a matrix.

        J = np.array([
            [Fa, Fb],
            [Ga, Gb]
        ])
        return J

    

    

def newton_raphson_2d(function, jacobian, initialpoint,tol=1e-8,max_iter=100):
#set a starting point
    i = initialpoint
    a = i[0]
    b = i[1]
    iterations = 0
    point = [a,b]
#Repeat until the answer is close enough or the limit is reached.
    while iterations < max_iter:
            
#Calculate the next step.
            delta = np.linalg.solve(jacobian(point), -function(point))
#Update alpha and beta.
            point = point + delta
            iterations += 1
#Check how close the number to zero
            max_abs_value = np.max(np.abs(function(point)))
            if(max_abs_value < tol):
                break
    return point, iterations, max_abs_value


def newton_raphson(function, jacobian, initialPoint, tol=1e-8, max_iter=100):
 #Set the starting point.
    I = initialPoint
    xk = I[0]
    yk = I[1]
    zk = I[2]
    iterations = 0
    #Repeat until the answer is close enough or the limit is reached.

    point = np.array([xk, yk, zk], dtype=float)
    iterations = 0
    max_abs_value = np.max(np.abs(function(point)))
    while iterations < max_iter:
    # Calculate the next step.

        delta = np.linalg.solve(jacobian(point), -function(point))
        point = point + delta
        iterations += 1
    # Check how close the answers are to zero.
        max_abs_value = np.max(np.abs(function(point)))
        if(max_abs_value < tol):
            break
    # Return the answer and iteration information.      
    return point, iterations, max_abs_value
        




    #f_par = ((3*x) - math.cos(y*z) - (1/2)) + (fx) * (x-xk) + (fy) * (y-yk) + fz * (z-zk)
    #g_par = ((x**2) - 81*(y+0.1)**2 + math.sin(z) + 1.06) + gx * (x-xk) + gy * (y-yk) + gz * (z-zk)
    #h_par = (math.e**(-(x*y)) + 20*z + ((10 * math.pi) - 3)/3) + hx * (x-xk) + hy * (y-yk) + hz * (z-zk)





def main():
    # Part 1: Solve the three equation
    ip = np.array([0.1,0.1,-0.1])
    point, iterations, max_abs_value = newton_raphson(functions, jacobians, ip)
    print(f"\nfinal point = {point}\niterations = {iterations}\n final max_abs_value = {max_abs_value}")
    # Part 2: Solve the logistic regression equation
    ip2 = np.array([0,0])
    point2, iterations2, max_abs_value2 = newton_raphson_2d(functions, jacobians, ip2)
    print("Part 2")
    print(f"\nfinal point = {point2}\niterations  = {iterations2}\n final max_abs_value = {max_abs_value2}")
    a_opt, b_opt = point2[0], point2[1]

    # Generate temperature values for a smooth curve
    temp_range = np.linspace(df['temp_f'].min() - 5, df['temp_f'].max() + 5, 200)

    # Calculate probability using logistic function: p = 1 / (1 + e^-(a + b*t))
    prob_curve = 1 / (1 + np.exp(-(a_opt + b_opt * temp_range)))

    # Create the plot
    plt.figure(figsize=(10, 6))

    # Plot the actual data points
    plt.scatter(df['temp_f'], df['distress'], color='blue', alpha=0.7, label='Actual Data (Distress: 1, Normal: 0)', zorder=3)

    # Plot the fitted logistic curve
    plt.plot(temp_range, prob_curve, color='red', linewidth=2, label=f'Fitted Logistic Curve\n$p(T) = 1 / (1 + e^{{-({a_opt:.4f} {b_opt:+.4f} T)}})$')

    # Add labels and formatting
    plt.title('O-Ring Thermal Distress Probability vs. Temperature', fontsize=14)
    plt.xlabel('Temperature (°F)', fontsize=12)
    plt.ylabel('Probability of Distress', fontsize=12)
    plt.axhline(0.5, color='gray', linestyle='--', alpha=0.5, label='Decision Boundary (p=0.5)')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(loc='best', fontsize=10)
    plt.show()



if __name__ == "__main__":
    main()